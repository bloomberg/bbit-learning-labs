# API Routes, Requests and Responses
### `/get_share_names/`
* Response should be an object with a key named `records`. Its value is an array of objects with keys `shareSymbol` and `shareName`, both strings.
```jsx
// E.g.
{ records: [ { shareSymbol: "GOOGL", shareName: "Google" }, /* ... */ ] }
```

### `/buy_share/`
* Request will be a POST request, and will have a body of the following structure:
    ```js
    share = {
        "symbol": string,
        "sharePrice": float,
        "1dChange": float,
        "yourShares": float,
        "avgPrice": float,
        "mktValue": float,
        "yourChange": float
    }
    ```
* This request should put the share in a database storage, or if already present, should add the existing shares amount with the newly purchased amount

### `/sell_shares/`
* Request will be a POST request, and the body will be an object with keys `shareSymbol` and `shareCount`, string and float values, respectively; e.g. 
    ```js
    {
        shareSymbol: "GOOGL",
        shareCount: 300
    }
    ```
* API should subtract share count from existing record, and if share count falls below 0, purge record from storage

### `/get_shares/`
* Response should be a list of share objects, like the ones showed above:
    ```js
    {
        "symbol": string,
        "sharePrice": float,
        "1dChange": float,
        "yourShares": float,
        "avgPrice": float,
        "mktValue": float,
        "yourChange": float
    }[]
    ```
### `/get_share_price/<string:symbol>`
* Response should be a string representation of the share price for share with `symbol`

### `/get_percentage_change/<string:symbol>`
* Response should be a string representation of the percentage change of a share with `symbol`
