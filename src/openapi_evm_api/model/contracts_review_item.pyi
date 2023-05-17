# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_evm_api import schemas  # noqa: F401


class ContractsReviewItem(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "contract_type",
            "reason",
            "report_type",
            "contract_address",
        }
        
        class properties:
            contract_address = schemas.StrSchema
            reason = schemas.StrSchema
            
            
            class report_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SPAM(cls):
                    return cls("spam")
                
                @schemas.classproperty
                def NOT_SPAM(cls):
                    return cls("not_spam")
            
            
            class contract_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ERC20(cls):
                    return cls("ERC20")
                
                @schemas.classproperty
                def NFT(cls):
                    return cls("NFT")
            __annotations__ = {
                "contract_address": contract_address,
                "reason": reason,
                "report_type": report_type,
                "contract_type": contract_type,
            }

    
    contract_type: MetaOapg.properties.contract_type
    reason: MetaOapg.properties.reason
    report_type: MetaOapg.properties.report_type
    contract_address: MetaOapg.properties.contract_address
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_address"]) -> MetaOapg.properties.contract_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["report_type"]) -> MetaOapg.properties.report_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_type"]) -> MetaOapg.properties.contract_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["contract_address", "reason", "report_type", "contract_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_address"]) -> MetaOapg.properties.contract_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["report_type"]) -> MetaOapg.properties.report_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_type"]) -> MetaOapg.properties.contract_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contract_address", "reason", "report_type", "contract_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        contract_type: typing.Union[MetaOapg.properties.contract_type, str, ],
        reason: typing.Union[MetaOapg.properties.reason, str, ],
        report_type: typing.Union[MetaOapg.properties.report_type, str, ],
        contract_address: typing.Union[MetaOapg.properties.contract_address, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContractsReviewItem':
        return super().__new__(
            cls,
            *args,
            contract_type=contract_type,
            reason=reason,
            report_type=report_type,
            contract_address=contract_address,
            _configuration=_configuration,
            **kwargs,
        )
