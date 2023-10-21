import pybgpstream
from collections import defaultdict

def fetch_asn_ip_mappings():
    asn_ip_mappings = defaultdict(list)
    stream = pybgpstream.BGPStream(
        project="ris-live",
        filter="collector rrc00",
    )
    for rec in stream:
        for elem in rec:
            if elem.type == "A":
                origin_asn = elem.fields["as-path"].split()[-1]
                prefix = elem.fields["prefix"]
                if prefix not in asn_ip_mappings[origin_asn]:
                    asn_ip_mappings[origin_asn].append(prefix)
                    print(f'{origin_asn} - {prefix}')
    return asn_ip_mappings

if __name__ == "__main__":
    mappings = fetch_asn_ip_mappings()
    for asn, prefixes in mappings.items():
        print(f"ASN: {asn}, Prefixes: {', '.join(prefixes)}")



