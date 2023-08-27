df.head()

	property_type	region	area_m2	price_usd	lat	lon	state
0	apartment	Northeast	110.0	187230.85	-9.644305	-35.708814	Alagoas
1	apartment	Northeast	65.0	81133.37	-9.643093	-35.704840	Alagoas
2	house	Northeast	211.0	154465.45	-9.622703	-35.729795	Alagoas
3	apartment	Northeast	99.0	146013.20	-9.622837	-35.719556	Alagoas
4	apartment	Northeast	55.0	101416.71	-9.654955	-35.700227	Alagoas

dfa = df[["area_m2", "price_usd"]]  # subset for a data frame
summary_stats = dfa.describe()
summary_stats

	     area_m2	     price_usd
count	22844.000000	  22844.000000
mean	115.020224	    194987.315480
std	  47.742932	      103617.682978
min	  53.000000	      74892.340000
25%	  76.000000	      113898.770000
50%	  103.000000	    165697.555000
75%	  142.000000	    246900.880878
max	  252.000000	    525659.717868
