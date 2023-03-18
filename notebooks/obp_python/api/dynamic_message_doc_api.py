# coding: utf-8

"""
    Open Bank Project API

    An Open Source API for Banks. (c) TESOBE GmbH. 2011 - 2022. Licensed under the AGPL and commercial licences.  # noqa: E501

    OpenAPI spec version: v5.0.0
    Contact: contact@tesobe.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from obp_python.api_client import ApiClient


class DynamicMessageDocApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_bank_level_dynamic_message_doc(self, body, bank_id, **kwargs):  # noqa: E501
        """Create Bank Level Dynamic Message Doc  # noqa: E501

        <p>Create a Bank Level Dynamic Message Doc.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_bank_level_dynamic_message_doc(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JsonDynamicMessageDoc body: JsonDynamicMessageDoc object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: JsonDynamicMessageDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_bank_level_dynamic_message_doc_with_http_info(body, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_bank_level_dynamic_message_doc_with_http_info(body, bank_id, **kwargs)  # noqa: E501
            return data

    def create_bank_level_dynamic_message_doc_with_http_info(self, body, bank_id, **kwargs):  # noqa: E501
        """Create Bank Level Dynamic Message Doc  # noqa: E501

        <p>Create a Bank Level Dynamic Message Doc.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_bank_level_dynamic_message_doc_with_http_info(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JsonDynamicMessageDoc body: JsonDynamicMessageDoc object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: JsonDynamicMessageDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_bank_level_dynamic_message_doc" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_bank_level_dynamic_message_doc`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `create_bank_level_dynamic_message_doc`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/management/banks/{BANK_ID}/dynamic-message-docs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonDynamicMessageDoc',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_dynamic_message_doc(self, body, **kwargs):  # noqa: E501
        """Create Dynamic Message Doc  # noqa: E501

        <p>Create a Dynamic Message Doc.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_dynamic_message_doc(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JsonDynamicMessageDoc body: JsonDynamicMessageDoc object that needs to be added. (required)
        :return: JsonDynamicMessageDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_dynamic_message_doc_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_dynamic_message_doc_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_dynamic_message_doc_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Dynamic Message Doc  # noqa: E501

        <p>Create a Dynamic Message Doc.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_dynamic_message_doc_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JsonDynamicMessageDoc body: JsonDynamicMessageDoc object that needs to be added. (required)
        :return: JsonDynamicMessageDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dynamic_message_doc" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_dynamic_message_doc`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/management/dynamic-message-docs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonDynamicMessageDoc',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_bank_level_dynamic_message_doc(self, bank_id, **kwargs):  # noqa: E501
        """Delete Bank Level Dynamic Message Doc  # noqa: E501

        <p>Delete a Bank Level Dynamic Message Doc.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bank_level_dynamic_message_doc(bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bank_id: The bank id (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_bank_level_dynamic_message_doc_with_http_info(bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_bank_level_dynamic_message_doc_with_http_info(bank_id, **kwargs)  # noqa: E501
            return data

    def delete_bank_level_dynamic_message_doc_with_http_info(self, bank_id, **kwargs):  # noqa: E501
        """Delete Bank Level Dynamic Message Doc  # noqa: E501

        <p>Delete a Bank Level Dynamic Message Doc.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bank_level_dynamic_message_doc_with_http_info(bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bank_id: The bank id (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bank_level_dynamic_message_doc" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `delete_bank_level_dynamic_message_doc`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/management/banks/{BANK_ID}/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_dynamic_message_doc(self, **kwargs):  # noqa: E501
        """Delete Dynamic Message Doc  # noqa: E501

        <p>Delete a Dynamic Message Doc.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dynamic_message_doc(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_dynamic_message_doc_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_dynamic_message_doc_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_dynamic_message_doc_with_http_info(self, **kwargs):  # noqa: E501
        """Delete Dynamic Message Doc  # noqa: E501

        <p>Delete a Dynamic Message Doc.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dynamic_message_doc_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dynamic_message_doc" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/management/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_bank_level_dynamic_message_docs(self, bank_id, **kwargs):  # noqa: E501
        """Get all Bank Level Dynamic Message Docs  # noqa: E501

        <p>Get all Bank Level Dynamic Message Docs.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_bank_level_dynamic_message_docs(bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bank_id: The bank id (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_bank_level_dynamic_message_docs_with_http_info(bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_bank_level_dynamic_message_docs_with_http_info(bank_id, **kwargs)  # noqa: E501
            return data

    def get_all_bank_level_dynamic_message_docs_with_http_info(self, bank_id, **kwargs):  # noqa: E501
        """Get all Bank Level Dynamic Message Docs  # noqa: E501

        <p>Get all Bank Level Dynamic Message Docs.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_bank_level_dynamic_message_docs_with_http_info(bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bank_id: The bank id (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_bank_level_dynamic_message_docs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `get_all_bank_level_dynamic_message_docs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/management/banks/{BANK_ID}/dynamic-message-docs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_dynamic_message_docs(self, **kwargs):  # noqa: E501
        """Get all Dynamic Message Docs  # noqa: E501

        <p>Get all Dynamic Message Docs.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_dynamic_message_docs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_dynamic_message_docs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_dynamic_message_docs_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_dynamic_message_docs_with_http_info(self, **kwargs):  # noqa: E501
        """Get all Dynamic Message Docs  # noqa: E501

        <p>Get all Dynamic Message Docs.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_dynamic_message_docs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_dynamic_message_docs" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/management/dynamic-message-docs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bank_level_dynamic_message_doc(self, bank_id, **kwargs):  # noqa: E501
        """Get Bank Level Dynamic Message Doc  # noqa: E501

        <p>Get a Bank Level Dynamic Message Doc by DYNAMIC_MESSAGE_DOC_ID.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bank_level_dynamic_message_doc(bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bank_id: The bank id (required)
        :return: JsonDynamicMessageDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bank_level_dynamic_message_doc_with_http_info(bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bank_level_dynamic_message_doc_with_http_info(bank_id, **kwargs)  # noqa: E501
            return data

    def get_bank_level_dynamic_message_doc_with_http_info(self, bank_id, **kwargs):  # noqa: E501
        """Get Bank Level Dynamic Message Doc  # noqa: E501

        <p>Get a Bank Level Dynamic Message Doc by DYNAMIC_MESSAGE_DOC_ID.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bank_level_dynamic_message_doc_with_http_info(bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bank_id: The bank id (required)
        :return: JsonDynamicMessageDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bank_level_dynamic_message_doc" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `get_bank_level_dynamic_message_doc`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/management/banks/{BANK_ID}/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonDynamicMessageDoc',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dynamic_message_doc(self, **kwargs):  # noqa: E501
        """Get Dynamic Message Doc  # noqa: E501

        <p>Get a Dynamic Message Doc by DYNAMIC_MESSAGE_DOC_ID.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dynamic_message_doc(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: JsonDynamicMessageDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dynamic_message_doc_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_dynamic_message_doc_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_dynamic_message_doc_with_http_info(self, **kwargs):  # noqa: E501
        """Get Dynamic Message Doc  # noqa: E501

        <p>Get a Dynamic Message Doc by DYNAMIC_MESSAGE_DOC_ID.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dynamic_message_doc_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: JsonDynamicMessageDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dynamic_message_doc" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/management/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonDynamicMessageDoc',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_bank_level_dynamic_message_doc(self, body, bank_id, **kwargs):  # noqa: E501
        """Update Bank Level Dynamic Message Doc  # noqa: E501

        <p>Update a Bank Level Dynamic Message Doc.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_bank_level_dynamic_message_doc(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JsonDynamicMessageDoc body: JsonDynamicMessageDoc object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: JsonDynamicMessageDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_bank_level_dynamic_message_doc_with_http_info(body, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_bank_level_dynamic_message_doc_with_http_info(body, bank_id, **kwargs)  # noqa: E501
            return data

    def update_bank_level_dynamic_message_doc_with_http_info(self, body, bank_id, **kwargs):  # noqa: E501
        """Update Bank Level Dynamic Message Doc  # noqa: E501

        <p>Update a Bank Level Dynamic Message Doc.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_bank_level_dynamic_message_doc_with_http_info(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JsonDynamicMessageDoc body: JsonDynamicMessageDoc object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: JsonDynamicMessageDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_bank_level_dynamic_message_doc" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `update_bank_level_dynamic_message_doc`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `update_bank_level_dynamic_message_doc`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/management/banks/{BANK_ID}/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonDynamicMessageDoc',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_dynamic_message_doc(self, body, **kwargs):  # noqa: E501
        """Update Dynamic Message Doc  # noqa: E501

        <p>Update a Dynamic Message Doc.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dynamic_message_doc(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JsonDynamicMessageDoc body: JsonDynamicMessageDoc object that needs to be added. (required)
        :return: JsonDynamicMessageDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_dynamic_message_doc_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dynamic_message_doc_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_dynamic_message_doc_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update Dynamic Message Doc  # noqa: E501

        <p>Update a Dynamic Message Doc.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dynamic_message_doc_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JsonDynamicMessageDoc body: JsonDynamicMessageDoc object that needs to be added. (required)
        :return: JsonDynamicMessageDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dynamic_message_doc" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `update_dynamic_message_doc`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/management/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonDynamicMessageDoc',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
