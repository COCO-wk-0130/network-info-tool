import unittest
import socket
from unittest.mock import patch
from ipaddress import ip_network
from main import parse_ip_input, get_usable_hosts, lookup_hostname


class TestIPParsing(unittest.TestCase):

    def test_ipv4_without_cidr(self):
        ip, network = parse_ip_input("192.168.1.10")

        self.assertEqual(str(ip), "192.168.1.10")
        self.assertIsNone(network)

    def test_ipv4_with_cidr(self):
        ip, network = parse_ip_input("192.168.1.42/26")

        self.assertEqual(str(ip), "192.168.1.42")
        self.assertEqual(str(network), "192.168.1.0/26")

    def test_ipv6_without_cidr(self):
        ip, network = parse_ip_input("2001:db8::1")

        self.assertEqual(ip.version, 6)
        self.assertIsNone(network)

    def test_ipv6_with_cidr(self):
        ip, network = parse_ip_input("2001:db8::1/64")

        self.assertEqual(ip.version, 6)
        self.assertEqual(str(network), "2001:db8::/64")

    def test_invalid_ip(self):
        with self.assertRaises(ValueError):
            parse_ip_input("999.999.999.999")

    def test_invalid_cidr(self):
        with self.assertRaises(ValueError):
            parse_ip_input("192.168.1.1/33")

class TestSubnetCalculation(unittest.TestCase):

    def test_usable_host(self):
        test_list = [
            ("192.168.1.0/24", 254),
            ("192.168.1.0/26", 62),
            ("192.168.1.0/30", 2),
            ("192.168.1.0/31", 2),
            ("192.168.1.0/32", 1),
        ]

        for cidr, expected in test_list:
            with self.subTest(cidr=cidr):
                network = ip_network(cidr)
                self.assertEqual(get_usable_hosts(network), expected)

    def test_ipv6_usable_hosts(self):
        network = ip_network("2001:db8::/64")

        with self.assertRaises(ValueError):
            get_usable_hosts(network)

class TestDNSLookup(unittest.TestCase):

    @patch("main.socket.gethostbyaddr")
    def test_successful_lookup(self, mock_dns):
        mock_dns.return_value = (
            "dns.google",
            [],
            ["8.8.8.8"]
        )

        hostname, aliases, addresses = lookup_hostname("8.8.8.8")

        self.assertEqual(hostname, "dns.google")
        self.assertEqual(addresses, ["8.8.8.8"])
    
    @patch("main.socket.gethostbyaddr")
    def test_failed_lookup(self, mock_dns):
        mock_dns.side_effect = socket.herror("No PTR record")

        hostname, aliases, addresses = lookup_hostname("192.0.2.1")

        self.assertIsNone(hostname)
        self.assertIsNone(aliases)
        self.assertIsNone(addresses)

    