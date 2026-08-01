import os
import sys
import cv2

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.DemoPackageMih.src.models.PackageModel import PackageModel
from components.DemoPackageMih.src.utils.response import build_response_gray


class GrayExecutor(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.image = self.request.get_param("inputImageOne")
        self.method = self.request.get_param("demoDependentDropdown")

        if self.method == "OptionA":
            self.val_int = self.request.get_param("optionAIntegerField")
            self.val_bool = self.request.get_param("optionABoolField")
        else:
            self.val_float = self.request.get_param("optionBFloatField")
            self.val_string = self.request.get_param("optionBStringField")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def process(self, img):
        """
        Görseli gri tona dönüştürür
        """
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)

        img.value = self.process(img.value)

        self.output_image_one = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)

        packageModel = build_response_gray(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()