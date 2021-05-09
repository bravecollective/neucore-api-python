"""
    Neucore API

    Client library of Neucore API  # noqa: E501

    The version of the OpenAPI document: 1.21.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from neucore_api.api_client import ApiClient, Endpoint as _Endpoint
from neucore_api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)


class ApplicationESIApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __esi_post_v1(
            self,
            esi_path_query,
            datasource,
            body,
            **kwargs
        ):
            """Same as GET /app/v1/esi, but for POST requests.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.esi_post_v1(esi_path_query, datasource, body, async_req=True)
            >>> result = thread.get()

            Args:
                esi_path_query (str): The ESI path and query string (without the datasource parameter).
                datasource (str): The EVE character ID those token should be used to make the ESI request
                body (str): JSON encoded data.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                str
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['esi_path_query'] = \
                esi_path_query
            kwargs['datasource'] = \
                datasource
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.esi_post_v1 = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/app/v1/esi',
                'operation_id': 'esi_post_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'esi_path_query',
                    'datasource',
                    'body',
                ],
                'required': [
                    'esi_path_query',
                    'datasource',
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'esi_path_query':
                        (str,),
                    'datasource':
                        (str,),
                    'body':
                        (str,),
                },
                'attribute_map': {
                    'esi_path_query': 'esi-path-query',
                    'datasource': 'datasource',
                },
                'location_map': {
                    'esi_path_query': 'query',
                    'datasource': 'query',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'text/plain'
                ]
            },
            api_client=api_client,
            callable=__esi_post_v1
        )

        def __esi_v1(
            self,
            esi_path_query,
            datasource,
            **kwargs
        ):
            """Makes an ESI GET request on behalf on an EVE character and returns the result.  # noqa: E501

            Needs role: app-esi<br>      *         Public ESI routes are not allowed.<br>      *         The following headers from ESI are passed through to the response if they exist:                Content-Type Expires X-Esi-Error-Limit-Remain X-Esi-Error-Limit-Reset X-Pages warning, Warning<br>      *         The HTTP status code from ESI is also passed through, so there may be more than the documented ones.<br>      *         The ESI path and query parameters can alternatively be appended to the path of this endpoint,                this allows to use OpenAPI clients that were generated for the ESI API,                see doc/app-esi-examples.php for more.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.esi_v1(esi_path_query, datasource, async_req=True)
            >>> result = thread.get()

            Args:
                esi_path_query (str): The ESI path and query string (without the datasource parameter).
                datasource (str): The EVE character ID those token should be used to make the ESI request

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                str
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['esi_path_query'] = \
                esi_path_query
            kwargs['datasource'] = \
                datasource
            return self.call_with_http_info(**kwargs)

        self.esi_v1 = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/app/v1/esi',
                'operation_id': 'esi_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'esi_path_query',
                    'datasource',
                ],
                'required': [
                    'esi_path_query',
                    'datasource',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'esi_path_query':
                        (str,),
                    'datasource':
                        (str,),
                },
                'attribute_map': {
                    'esi_path_query': 'esi-path-query',
                    'datasource': 'datasource',
                },
                'location_map': {
                    'esi_path_query': 'query',
                    'datasource': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__esi_v1
        )