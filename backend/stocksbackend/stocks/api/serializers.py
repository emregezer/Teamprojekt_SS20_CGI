from django.utils import timezone
from rest_framework import serializers
from stocks.models import Stock, Price


class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            "symbol",
            "company_name",
        ]


class PricesSerializer(serializers.ModelSerializer):
    p_low = serializers.DecimalField(
        max_digits=8, decimal_places=3, coerce_to_string=False
    )
    p_open = serializers.DecimalField(
        max_digits=8, decimal_places=3, coerce_to_string=False
    )
    p_high = serializers.DecimalField(
        max_digits=8, decimal_places=3, coerce_to_string=False
    )
    p_close = serializers.DecimalField(
        max_digits=8, decimal_places=3, coerce_to_string=False
    )

    class Meta:
        model = Price
        fields = [
            "date",
            "exchange_time",
            "p_low",
            "p_open",
            "p_high",
            "p_close",
            "volume",
        ]
