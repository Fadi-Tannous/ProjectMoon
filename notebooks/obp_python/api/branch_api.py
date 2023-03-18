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


class BranchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_branch(self, body, bank_id, **kwargs):  # noqa: E501
        """Create Branch  # noqa: E501

        <p>Create Branch for the Bank.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_branch(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BranchJsonV300 body: BranchJsonV300 object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: BranchJsonV300
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_branch_with_http_info(body, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_branch_with_http_info(body, bank_id, **kwargs)  # noqa: E501
            return data

    def create_branch_with_http_info(self, body, bank_id, **kwargs):  # noqa: E501
        """Create Branch  # noqa: E501

        <p>Create Branch for the Bank.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_branch_with_http_info(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BranchJsonV300 body: BranchJsonV300 object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: BranchJsonV300
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
                    " to method create_branch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_branch`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `create_branch`")  # noqa: E501

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
            '/obp/v5.0.0/banks/{BANK_ID}/branches', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BranchJsonV300',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_branch(self, body, branch_id, bank_id, **kwargs):  # noqa: E501
        """Delete Branch  # noqa: E501

        <p>Delete Branch from given Bank.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_branch(body, branch_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmptyClassJson body: EmptyClassJson object that needs to be added. (required)
        :param str branch_id: The branch id (required)
        :param str bank_id: The bank id (required)
        :return: EmptyClassJson
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_branch_with_http_info(body, branch_id, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_branch_with_http_info(body, branch_id, bank_id, **kwargs)  # noqa: E501
            return data

    def delete_branch_with_http_info(self, body, branch_id, bank_id, **kwargs):  # noqa: E501
        """Delete Branch  # noqa: E501

        <p>Delete Branch from given Bank.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_branch_with_http_info(body, branch_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmptyClassJson body: EmptyClassJson object that needs to be added. (required)
        :param str branch_id: The branch id (required)
        :param str bank_id: The bank id (required)
        :return: EmptyClassJson
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'branch_id', 'bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_branch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `delete_branch`")  # noqa: E501
        # verify the required parameter 'branch_id' is set
        if self.api_client.client_side_validation and ('branch_id' not in params or
                                                       params['branch_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `branch_id` when calling `delete_branch`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `delete_branch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'branch_id' in params:
            path_params['BRANCH_ID'] = params['branch_id']  # noqa: E501
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
            '/obp/v5.0.0/banks/{BANK_ID}/branches/{BRANCH_ID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmptyClassJson',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_branch(self, body, branch_id, bank_id, **kwargs):  # noqa: E501
        """Get Branch  # noqa: E501

        <p>Returns information about a single Branch specified by BANK_ID and BRANCH_ID including:</p><ul><li>Name</li><li>Address</li><li>Geo Location</li><li>License the data under this endpoint is released under.</li></ul><p>Authentication is Optional</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_branch(body, branch_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmptyClassJson body: EmptyClassJson object that needs to be added. (required)
        :param str branch_id: The branch id (required)
        :param str bank_id: The bank id (required)
        :return: BranchJsonV300
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_branch_with_http_info(body, branch_id, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_branch_with_http_info(body, branch_id, bank_id, **kwargs)  # noqa: E501
            return data

    def get_branch_with_http_info(self, body, branch_id, bank_id, **kwargs):  # noqa: E501
        """Get Branch  # noqa: E501

        <p>Returns information about a single Branch specified by BANK_ID and BRANCH_ID including:</p><ul><li>Name</li><li>Address</li><li>Geo Location</li><li>License the data under this endpoint is released under.</li></ul><p>Authentication is Optional</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_branch_with_http_info(body, branch_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmptyClassJson body: EmptyClassJson object that needs to be added. (required)
        :param str branch_id: The branch id (required)
        :param str bank_id: The bank id (required)
        :return: BranchJsonV300
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'branch_id', 'bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_branch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `get_branch`")  # noqa: E501
        # verify the required parameter 'branch_id' is set
        if self.api_client.client_side_validation and ('branch_id' not in params or
                                                       params['branch_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `branch_id` when calling `get_branch`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `get_branch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'branch_id' in params:
            path_params['BRANCH_ID'] = params['branch_id']  # noqa: E501
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
            '/obp/v5.0.0/banks/{BANK_ID}/branches/{BRANCH_ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BranchJsonV300',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_branches(self, body, bank_id, **kwargs):  # noqa: E501
        """Get Branches for a Bank  # noqa: E501

        <p>Returns information about branches for a single bank specified by BANK_ID including:</p><ul><li>Name</li><li>Address</li><li>Geo Location</li><li>License the data under this endpoint is released under</li><li>Structured opening hours</li><li>Accessible flag</li><li>Branch Type</li><li>More Info</li></ul><p>Pagination:</p><p>By default, 50 records are returned.</p><p>You can use the url query parameters <em>limit</em> and <em>offset</em> for pagination<br />You can also use the follow url query parameters:</p><ul><li><p>city - string, find Branches those in this city, optional</p></li><li><p>withinMetersOf - number, find Branches within given meters distance, optional</p></li><li>nearLatitude - number, a position of latitude value, cooperate with withMetersOf do query filter, optional</li><li>nearLongitude - number, a position of longitude value, cooperate with withMetersOf do query filter, optional</li></ul><p>note: withinMetersOf, nearLatitude and nearLongitude either all empty or all have value.</p><p>Authentication is Optional</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_branches(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmptyClassJson body: EmptyClassJson object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: BranchesJsonV300
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_branches_with_http_info(body, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_branches_with_http_info(body, bank_id, **kwargs)  # noqa: E501
            return data

    def get_branches_with_http_info(self, body, bank_id, **kwargs):  # noqa: E501
        """Get Branches for a Bank  # noqa: E501

        <p>Returns information about branches for a single bank specified by BANK_ID including:</p><ul><li>Name</li><li>Address</li><li>Geo Location</li><li>License the data under this endpoint is released under</li><li>Structured opening hours</li><li>Accessible flag</li><li>Branch Type</li><li>More Info</li></ul><p>Pagination:</p><p>By default, 50 records are returned.</p><p>You can use the url query parameters <em>limit</em> and <em>offset</em> for pagination<br />You can also use the follow url query parameters:</p><ul><li><p>city - string, find Branches those in this city, optional</p></li><li><p>withinMetersOf - number, find Branches within given meters distance, optional</p></li><li>nearLatitude - number, a position of latitude value, cooperate with withMetersOf do query filter, optional</li><li>nearLongitude - number, a position of longitude value, cooperate with withMetersOf do query filter, optional</li></ul><p>note: withinMetersOf, nearLatitude and nearLongitude either all empty or all have value.</p><p>Authentication is Optional</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_branches_with_http_info(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmptyClassJson body: EmptyClassJson object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: BranchesJsonV300
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
                    " to method get_branches" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `get_branches`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `get_branches`")  # noqa: E501

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
            '/obp/v5.0.0/banks/{BANK_ID}/branches', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BranchesJsonV300',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
