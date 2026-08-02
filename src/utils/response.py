from sdks.novavision.src.helper.package import PackageHelper
from components.DemoPackageMih.src.models.PackageModel import (
    PackageModel, PackageConfigs, ConfigExecutor,
    GrayExecutor, GrayExecutorResponse, GrayExecutorOutputs, OutputImageOne,
    MixExecutor, MixExecutorResponse, MixExecutorOutputs, OutputImageTwo,
)

def build_response_gray(context):
    outputImageOne = OutputImageOne(value=context.image)
    grayExecutorOutputs = GrayExecutorOutputs(outputImageOne=outputImageOne)
    grayexecutorResponse = GrayExecutorResponse(outputs=grayExecutorOutputs)
    grayExecutor = GrayExecutor(value=grayexecutorResponse)
    configExecutor = ConfigExecutor(value=grayExecutor)
    packageConfigs = PackageConfigs(executor=configExecutor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel

def build_response_mix(context):
    outputImageOne = OutputImageOne(value=context.image_one)
    outputImageTwo = OutputImageTwo(value=context.image_two)
    mixExecutorOutputs = MixExecutorOutputs(outputImageOne=outputImageOne, outputImageTwo=outputImageTwo)
    mixExecutorResponse = MixExecutorResponse(outputs=mixExecutorOutputs)
    mixExecutor = MixExecutor(value=mixExecutorResponse)
    configExecutor = ConfigExecutor(value=mixExecutor)
    packageConfigs = PackageConfigs(executor=configExecutor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel