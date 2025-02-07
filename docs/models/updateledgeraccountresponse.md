# UpdateLedgerAccountResponse

LedgerAccount updated


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `status_code`                              | *int*                                      | :heavy_check_mark:                         | HTTP Response Status Code                  | 200                                        |
| `status`                                   | *str*                                      | :heavy_check_mark:                         | HTTP Response Status                       | OK                                         |
| `service`                                  | *str*                                      | :heavy_check_mark:                         | Apideck ID of service provider             | xero                                       |
| `resource`                                 | *str*                                      | :heavy_check_mark:                         | Unified API resource name                  | ledger-accounts                            |
| `operation`                                | *str*                                      | :heavy_check_mark:                         | Operation performed                        | update                                     |
| `data`                                     | [models.UnifiedID](../models/unifiedid.md) | :heavy_check_mark:                         | N/A                                        |                                            |