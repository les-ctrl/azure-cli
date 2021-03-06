# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def billing_exception_handler(ex):
    from azure.mgmt.billing.models import ErrorResponse
    if isinstance(ex, ErrorResponse):
        message = ex.error.error.message
        raise CLIError(message)
    import sys
    from six import reraise
    reraise(*sys.exc_info())
