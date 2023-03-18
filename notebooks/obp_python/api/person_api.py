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


class PersonApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_customer(self, body, bank_id, **kwargs):  # noqa: E501
        """Create Customer  # noqa: E501

        <p>The Customer resource stores the customer number (which is set by the backend), legal name, email, phone number, their date of birth, relationship status, education attained, a url for a profile image, KYC status etc.<br />Dates need to be in the format 2013-01-21T23:08:00Z</p><p>Note: If you need to set a specific customer number, use the Update Customer Number endpoint after this call.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_customer(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostCustomerJsonV500 body: PostCustomerJsonV500 object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: CustomerJsonV310
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_customer_with_http_info(body, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_customer_with_http_info(body, bank_id, **kwargs)  # noqa: E501
            return data

    def create_customer_with_http_info(self, body, bank_id, **kwargs):  # noqa: E501
        """Create Customer  # noqa: E501

        <p>The Customer resource stores the customer number (which is set by the backend), legal name, email, phone number, their date of birth, relationship status, education attained, a url for a profile image, KYC status etc.<br />Dates need to be in the format 2013-01-21T23:08:00Z</p><p>Note: If you need to set a specific customer number, use the Update Customer Number endpoint after this call.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_customer_with_http_info(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostCustomerJsonV500 body: PostCustomerJsonV500 object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: CustomerJsonV310
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
                    " to method create_customer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_customer`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `create_customer`")  # noqa: E501

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
            '/obp/v5.0.0/banks/{BANK_ID}/customers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomerJsonV310',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_customer_message(self, body, customer_id, bank_id, **kwargs):  # noqa: E501
        """Create Customer Message  # noqa: E501

        <p>Create a message for the customer specified by CUSTOMER_ID</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_customer_message(body, customer_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddCustomerMessageJson body: AddCustomerMessageJson object that needs to be added. (required)
        :param str customer_id: The customer id (required)
        :param str bank_id: The bank id (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_customer_message_with_http_info(body, customer_id, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_customer_message_with_http_info(body, customer_id, bank_id, **kwargs)  # noqa: E501
            return data

    def create_customer_message_with_http_info(self, body, customer_id, bank_id, **kwargs):  # noqa: E501
        """Create Customer Message  # noqa: E501

        <p>Create a message for the customer specified by CUSTOMER_ID</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_customer_message_with_http_info(body, customer_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddCustomerMessageJson body: AddCustomerMessageJson object that needs to be added. (required)
        :param str customer_id: The customer id (required)
        :param str bank_id: The bank id (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'customer_id', 'bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_customer_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_customer_message`")  # noqa: E501
        # verify the required parameter 'customer_id' is set
        if self.api_client.client_side_validation and ('customer_id' not in params or
                                                       params['customer_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `customer_id` when calling `create_customer_message`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `create_customer_message`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['CUSTOMER_ID'] = params['customer_id']  # noqa: E501
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
            '/obp/v5.0.0/banks/{BANK_ID}/customer/{CUSTOMER_ID}/messages', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessMessage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_customer_message_0(self, body, customer_id, bank_id, **kwargs):  # noqa: E501
        """Create Customer Message  # noqa: E501

        <p>Create a message for the customer specified by CUSTOMER_ID<br />Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_customer_message_0(body, customer_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateMessageJsonV400 body: CreateMessageJsonV400 object that needs to be added. (required)
        :param str customer_id: The customer id (required)
        :param str bank_id: The bank id (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_customer_message_0_with_http_info(body, customer_id, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_customer_message_0_with_http_info(body, customer_id, bank_id, **kwargs)  # noqa: E501
            return data

    def create_customer_message_0_with_http_info(self, body, customer_id, bank_id, **kwargs):  # noqa: E501
        """Create Customer Message  # noqa: E501

        <p>Create a message for the customer specified by CUSTOMER_ID<br />Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_customer_message_0_with_http_info(body, customer_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateMessageJsonV400 body: CreateMessageJsonV400 object that needs to be added. (required)
        :param str customer_id: The customer id (required)
        :param str bank_id: The bank id (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'customer_id', 'bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_customer_message_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_customer_message_0`")  # noqa: E501
        # verify the required parameter 'customer_id' is set
        if self.api_client.client_side_validation and ('customer_id' not in params or
                                                       params['customer_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `customer_id` when calling `create_customer_message_0`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `create_customer_message_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['CUSTOMER_ID'] = params['customer_id']  # noqa: E501
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
            '/obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/messages', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessMessage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
