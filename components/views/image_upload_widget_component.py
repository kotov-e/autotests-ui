from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from components.views.empy_view_component import EmptyViewComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.image import Image
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.identifier = identifier

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        # Картинка предпросмотра и блок предпросмотра картинки курса
        self.preview_image = Image(
            page=page,
            locator=f'{identifier}-image-upload-widget-preview-image',
            name='Image'
        )

        # Кнопка загрузки, удаления картинки предпросмотра курса и блок с инфо о загружаемой картинке
        self.image_upload_info_icon = Icon(
            page=page,
            locator=f'{identifier}-image-upload-widget-info-icon',
            name='Icon'
        )

        self.image_upload_info_title = Text(
            page=page,
            locator=f'{identifier}-image-upload-widget-info-title-text',
            name='Title'
        )

        self.image_upload_info_description = Text(
            page=page,
            locator=f'{identifier}-image-upload-widget-info-description-text',
            name='Description'
        )

        self.upload_button = Button(
            page=page,
            locator=f'{identifier}-image-upload-widget-upload-button',
            name='Button'
        )

        self.remove_button = Button(
            page=page,
            locator=f'{identifier}-image-upload-widget-remove-button',
            name='Button'
        )

        self.upload_input = FileInput(
            page=page,
            locator=f'{identifier}-image-upload-widget-input',
            name='Input'
        )

    def check_visible(self, is_image_uploaded: bool = False):
        self.image_upload_info_icon.check_visible()

        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text('Tap on "Upload image" button to select file')

        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text('Recommended file size 540X300')

        self.upload_button.check_visible()

        if is_image_uploaded:
            self.remove_button.check_visible()
            self.preview_image.check_visible()

        if not is_image_uploaded:
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here',

            )

    def click_remove_image_button(self):
        self.remove_button.click()

    def upload_preview_image(self, file: str):
        self.upload_input.set_input_files(file)