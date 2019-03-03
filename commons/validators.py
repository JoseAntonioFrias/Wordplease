import os

import magic
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from commons.enumerations import FileTypes
from commons.utils import get_extension_file


def validate_file_type(upload):

    tmp_path = 'tmp/%s' % upload.name[2:]

    # Salvamos el fichero en una carpeta temporal tmp
    full_tmp_path = save_file_temp(tmp_path, upload)

    # Obtenemos el tipo MIME usando python-magic.
    file_type_mime = get_type_mime(full_tmp_path, tmp_path)

    # extraemos la extension del fichero
    file_extension = get_extension_file(upload.name)

    # Obtenemos el tipo de fichero, Si es imagen, video u otro tipo.
    file_type = validate_file_extension(file_extension)

    # Obtenemos el tamaño del fichero
    file_size = upload.file.size

    # validamos el contenido
    if file_type == FileTypes.OTHER:
        raise ValidationError('El fichero de tipo {0} no es un una imagen o video soportado actualmente.'.
                              format(file_extension.upper()))
    elif file_type == FileTypes.IMAGE and file_type_mime not in settings.VALID_IMAGE_MIMETYPES:
        raise ValidationError('El contenido del fichero no es una imagen soportada. '
                              'JPEG, JPG, PNG o GIF son los recomendados.')
    elif file_type == FileTypes.VIDEO and file_type_mime not in settings.VALID_VIDEO_MIMETYPES:
        raise ValidationError('El contenido del fichero no es un video soportado. MP4, WEBM o OGG son los recomendados.')

    # validamos el tamaño máximo del fichero
    if file_type == FileTypes.IMAGE and file_type_mime in settings.VALID_IMAGE_MIMETYPES \
            and file_size > settings.MAX_SIZE_IMAGE:
        raise ValidationError('El tamaño de la imagen es mayor del límite máximo permitido. Tamaño máximo 0,5MB.')
    elif file_type == FileTypes.VIDEO and file_type_mime in settings.VALID_VIDEO_MIMETYPES \
            and file_size > settings.MAX_SIZE_VIDEO:
        raise ValidationError('El tamaño del video es mayor del límite máximo permitido. Tamaño máximo 2MB.')


def get_type_mime(full_tmp_path, tmp_path):
    file_type = magic.from_file(full_tmp_path, mime=True)
    default_storage.delete(tmp_path)

    return file_type


def save_file_temp(tmp_path, upload):
    default_storage.save(tmp_path, ContentFile(upload.file.read()))
    full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)

    return full_tmp_path


def validate_file_extension(extension):
    file_type = ''

    if extension in settings.VALID_IMAGE_EXTENSIONS:
        file_type = FileTypes.IMAGE
    elif extension in settings.VALID_VIDEO_EXTENSIONS:
        file_type = FileTypes.VIDEO
    else:
        file_type = FileTypes.OTHER

    return file_type
