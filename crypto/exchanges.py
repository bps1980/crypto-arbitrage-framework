import ccxt

exchanges = {
    'binanceus': ccxt.binanceus({
        'apiKey': 'SSYcfZc2JlPmuDEjQBIVnWTd2Q0OxJaTfSOceu0PIePewI2omqy6vQcy2UJcdYlh',
        'secret': 'p5IpZY8LdlQRu0UkZGqzIF7m2Fr78P0D0Xi2LTLz9lbQE1tV0eU9QKlrcEtSQpUR',
    }),
    'kucoin': ccxt.kucoin2({
        'apiKey': '621164f964ec94000137e3b7',
        'secret': 'c1c961b3-432f-45e6-9ee3-decbff1cf49a',
        'passphrase': 'Cruz@@2015',
    }),
    'kraken': ccxt.kraken({
        'apiKey': 'YExDcZLi7xWZrNZIxaRtVSU2AfV81lKUhfRnJm/AYhJWuKXiJ401Sn0b',
        'secret': 'cYCTStkF9TCIxwf8tUOW/e/fYKDUM2etRg3EuQfXS8ZwX7lvhGAXN14IdakcKyI/BgcU7rIG4LDz8IjwrCvUBg==',
    }),
    'coinbasepro': ccxt.coinbasepro({
        'apiKey': '611c43736efc14df32261964caf8d5c8',
        'secret': '8r6jbl+buX8MznaFpiN0SwTRBJnxpYmlLdlw0fJcQs3aIfX1+h6jTclcuofhogjx5Yb8sr7UpCeDQywUc82tyA==',
        'passphrase': 'xqb71b0w8xr',
    }),
    'cex': ccxt.cex({
        'apiKey': 'YCSxeKqDmus5FHqjiszTQxS5lA',
        'secret': '4xM1BuySaWApYhvwyc961aejF7Q',
    }),
}
