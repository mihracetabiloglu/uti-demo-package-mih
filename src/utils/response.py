from sdks.novavision.src.helper.package import PackageHelper
from components.Package.src.models.PackageModel import (
    PackageModel, PackageConfigs, ConfigExecutor,
    GrayExecutor, GrayExecutorResponse, GrayExecutorOutputs, OutputImageOne,
    MixExecutor, MixExecutorResponse, MixExecutorOutputs, OutputImageTwo,
)

def build_response_gray(context):
    outputImageOne = OutputImageOne(value=context.output_image_one)
    outputs = GrayExecutorOutputs(outputImageOne=outputImageOne)
    response = GrayExecutorResponse(outputs=outputs)
    grayExecutor = GrayExecutor(value=response)
    configExecutor = ConfigExecutor(value=grayExecutor)
    packageConfigs = PackageConfigs(executor=configExecutor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel

def build_response_mix(context):
    outputImageOne = OutputImageOne(value=context.output_image_one)
    outputImageTwo = OutputImageTwo(value=context.output_image_two)
    outputs = MixExecutorOutputs(outputImageOne=outputImageOne, outputImageTwo=outputImageTwo)
    response = MixExecutorResponse(outputs=outputs)
    mixExecutor = MixExecutor(value=response)
    configExecutor = ConfigExecutor(value=mixExecutor)
    packageConfigs = PackageConfigs(executor=configExecutor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel