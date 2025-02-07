# ConnectionSettings
(*vault.connection_settings*)

## Overview

### Available Operations

* [list](#list) - Get resource settings
* [update](#update) - Update settings

## list

This endpoint returns custom settings and their defaults required by connection for a given resource.


### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:
    res = apideck.vault.connection_settings.list(unified_api="crm", service_id="pipedrive", resource="leads")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `unified_api`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Unified API                                                         | crm                                                                 |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Service ID of the resource to return                                | pipedrive                                                           |
| `resource`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Name of the resource (plural)                                       | leads                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.VaultConnectionSettingsAllResponse](../../models/vaultconnectionsettingsallresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## update

Update default values for a connection's resource settings

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:
    res = apideck.vault.connection_settings.update(service_id="pipedrive", unified_api="crm", resource="leads", connection={
        "enabled": True,
        "settings": {
            "instance_url": "https://eu28.salesforce.com",
            "api_key": "12345xxxxxx",
        },
        "metadata": {
            "account": {
                "name": "My Company",
                "id": "c01458a5-7276-41ce-bc19-639906b0450a",
            },
            "plan": "enterprise",
        },
        "configuration": [
            {
                "resource": "leads",
                "defaults": [
                    {
                        "id": "ProductInterest",
                        "options": [
                            {
                                "id": "1234",
                                "label": "General Channel",
                                "options": [
                                    {
                                        "label": "General Channel",
                                        "value": 12.5,
                                    },
                                    {
                                        "label": "General Channel",
                                        "value": [
                                            "team",
                                            "general",
                                        ],
                                    },
                                ],
                            },
                        ],
                        "value": "GC5000 series",
                    },
                    {
                        "id": "ProductInterest",
                        "options": [
                            {
                                "label": "General Channel",
                                "value": 123,
                            },
                            {
                                "label": "General Channel",
                                "value": "general",
                            },
                            {
                                "id": "1234",
                                "label": "General Channel",
                                "options": [
                                    {
                                        "label": "General Channel",
                                        "value": 123,
                                    },
                                    {
                                        "label": "General Channel",
                                        "value": 12.5,
                                    },
                                    {
                                        "label": "General Channel",
                                        "value": True,
                                    },
                                ],
                            },
                        ],
                        "value": True,
                    },
                ],
            },
            {
                "resource": "leads",
                "defaults": [
                    {
                        "id": "ProductInterest",
                        "options": [
                            {
                                "id": "1234",
                                "label": "General Channel",
                                "options": [
                                    {
                                        "label": "General Channel",
                                        "value": 12.5,
                                    },
                                ],
                            },
                        ],
                        "value": True,
                    },
                ],
            },
            {
                "resource": "leads",
                "defaults": [
                    {
                        "id": "ProductInterest",
                        "options": [
                            {
                                "id": "1234",
                                "label": "General Channel",
                                "options": [
                                    {
                                        "label": "General Channel",
                                        "value": 123,
                                    },
                                ],
                            },
                        ],
                        "value": 10,
                    },
                    {
                        "id": "ProductInterest",
                        "options": [
                            {
                                "id": "1234",
                                "label": "General Channel",
                                "options": [
                                    {
                                        "label": "General Channel",
                                        "value": [
                                            "team",
                                            "general",
                                        ],
                                    },
                                    {
                                        "label": "General Channel",
                                        "value": True,
                                    },
                                    {
                                        "label": "General Channel",
                                        "value": 12.5,
                                    },
                                ],
                            },
                        ],
                        "value": 10,
                    },
                    {
                        "id": "ProductInterest",
                        "options": [
                            {
                                "id": "1234",
                                "label": "General Channel",
                                "options": [
                                    {
                                        "label": "General Channel",
                                        "value": [
                                            "team",
                                            "general",
                                        ],
                                    },
                                    {
                                        "label": "General Channel",
                                        "value": "general",
                                    },
                                ],
                            },
                            {
                                "label": "General Channel",
                                "value": 123,
                            },
                        ],
                        "value": True,
                    },
                ],
            },
        ],
        "custom_mappings": [
            {
                "value": "$.root.training.first_aid",
            },
        ],
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Service ID of the resource to return                                | pipedrive                                                           |
| `unified_api`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Unified API                                                         | crm                                                                 |
| `resource`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Name of the resource (plural)                                       | leads                                                               |
| `connection`                                                        | [models.ConnectionInput](../../models/connectioninput.md)           | :heavy_check_mark:                                                  | Fields that need to be updated on the resource                      |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.VaultConnectionSettingsUpdateResponse](../../models/vaultconnectionsettingsupdateresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |