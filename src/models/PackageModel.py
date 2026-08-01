from pydantic import Field, validator
from typing import List, Union, Literal, Optional
from sdks.novavision.src.base.model import Package, Image, Inputs, Configs, Outputs, Response, Request, Output, Input, Config

class InputImageOne(Input):
    name: Literal["inputImageOne"] = "inputImageOne"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type",pre=True, always=True)
    def set_type_based_on_value(cls,value,values):
        value=values.get('value')
        if isinstance(value,Image):
            return "object"
        elif isinstance(value,list):
            return "list"
        return "object"

    class Config:
        title = "Image Input 1"

class InputImageTwo(Input):
    name: Literal["inputImageTwo"] = "inputImageTwo"
    value: Union[List[Image], Image]
    type: str = "object"


    @validator("type",pre=True, always=True)
    def set_type_based_on_value(cls,value,values):
        value=values.get('value')
        if isinstance(value,Image):
            return "object"
        elif isinstance(value,list):
            return "list"
        return "object"

    class Config:
        title = "Image Input 2"

class OutputImageOne(Output):
    name: Literal["OutputImageOne"] = "OutputImageOne"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type",pre=True, always=True)
    def set_type_based_on_value(cls,value,values):
        value=values.get('value')
        if isinstance(value,Image):
            return "object"
        elif isinstance(value,list):
            return "list"
        return "object"

    class Config:
        title = "Result Output Image 1"

class OutputImageTwo(Output):
    name: Literal["OutputImageTwo"] = "OutputImageTwo"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type",pre=True, always=True)
    def set_type_based_on_value(cls,value,values):
        value=values.get('value')
        if isinstance(value,Image):
            return "object"
        elif isinstance(value,list):
            return "list"
        return "object"

    class Config:
        title = "Result Output Image 2"

class OptionAIntegerField(Config):
    name: Literal["OptionAIntegerField"] = "OptionAIntegerField"
    value: int = Field(default=10)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Integer Field for A"

class BoolOptionTrue(Config):
    name: Literal["True"] = "True"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"
    class Config:
        title = "Enable"

class BoolOptionFalse(Config):
    name: Literal["False"] = "False"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"
    class Config:
        title = "Disable"

class OptionABoolField(Config):
    name: Literal["OptionABoolField"] = "OptionABoolField"
    value: Union[BoolOptionTrue, BoolOptionFalse]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Boolean Field for A"
        json_schema_extra = {
            "target": "value"
        }

class OptionA(Config):
    name: Literal["OptionA"] = "OptionA"
    optionAIntegerField: OptionAIntegerField
    optionABoolField: OptionABoolField
    value: Literal["OptionA"] = "OptionA"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Method A"

class OptionBFloatField(Config):
    name: Literal["OptionBFloatField"] = "OptionBFloatField"
    value: float = Field(default=1.5)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Float Field for B"

class OptionBStringField(Config):
    name: Literal["OptionBStringField"] = "OptionBStringField"
    value: str = Field(default="default_string")
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "String Field for B"

class OptionB(Config):
    name: Literal["OptionB"] = "OptionB"
    optionBFloatField: OptionBFloatField
    optionBStringField: OptionBStringField
    value: Literal["OptionB"] = "OptionB"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "Method B"

class DemoDependentDropdown(Config):
    name: Literal["DemoDependentDropdown"] = "DemoDependentDropdown"
    value: Union[OptionA, OptionB]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"
    class Config:
        title = "Select Method"




class GrayExecutorInputs(Inputs):
    inputImageOne: InputImageOne

class MixExecutorInputs(Inputs):
    inputImageOne: InputImageOne
    inputImageTwo: InputImageTwo


class GrayExecutorConfigs(Configs):
    demoDependentDropdown: DemoDependentDropdown

class MixExecutorConfigs(Configs):
    demoDependentDropdown: DemoDependentDropdown

class GrayExecutorRequest(Request):
    inputs: Optional[GrayExecutorInputs]
    configs: GrayExecutorConfigs
    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class MixExecutorRequest(Request):
    inputs: Optional[MixExecutorInputs]
    configs: MixExecutorConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class GrayExecutorOutputs(Outputs):
    outputImageOne: OutputImageOne

class MixExecutorOutputs(Outputs):
    outputImageOne: OutputImageOne
    outputImageTwo: OutputImageTwo

class GrayExecutorResponse(Response):
    outputs: GrayExecutorOutputs

class MixExecutorResponse(Response):
    outputs: MixExecutorOutputs

class GrayExecutor(Config):
    name: Literal["GrayExecutor"] = "GrayExecutor"
    value: Union[GrayExecutorRequest, GrayExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "GrayExecutor"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }

class MixExecutor(Config):
    name: Literal["MixExecutor"] = "MixExecutor"
    value: Union[MixExecutorRequest, MixExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "MixExecutor"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }

class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[GrayExecutor, MixExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"

class PackageConfigs(Configs):
    executor: ConfigExecutor

class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["Package"] = "Package"