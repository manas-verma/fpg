# Implement the Candles API Endpoint

Welcome to the implementation part of the interview.

Here, you will create the API handler for the `/candles` endpoint and implement a storage
solution for candle data.

## Notes

- Please use the function skeleton in `src/api_handler.py` as the basis for your handler.
  
- You will only need to fetch candles from Coinbase via their REST API. 
  The endpoint is documented [here](https://docs.pro.coinbase.com/#get-historic-rates).
  
- You can use the function `get_one_minute_candles_from_coinbase` from `lib/candle_data` to fetch
    candle data from Coinbase.

- You can find a list of all supported currency pairs in `supported_currency_pairs.json`.

- If you need a database or cache, you can start them with docker compose: 
  - `docker-compose up postgres`
  - `docker-compose up dynamo`
  - `docker-compose up redis`

- You don't need to validate the inputs to your API handler. If we have time, we may ask to either
  implement that validation later or discuss how you would go about it.
  
- Coinbase only allows you to fetch five hours worth of one minute candles per request. You can
  initially assume that every request to your handler will ask for less than five hours worth 
  of candles. If you make good progress, we may then ask you to implement a version that fetches 
  a month or more worth of candles.

