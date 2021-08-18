from urllib.request import urlopen, Request
from urllib.error import URLError
import shutil
import tempfile
import urllib.request

# The site 'https://www.proxyscrape.com/free-proxy-list' provides free proxy list for http, Socks4 and Socks5
# https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all
# https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all
# https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all

URL_HTTP_PROXIES = "https://api.proxyscrape.com/v2/" \
      "?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"

URL_SOCKS4_PROXIES = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all"

URL_SOCKS5_PROXIES = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all"


def get_list_of_http_proxies(url):
    # Retrieve a resource via URL and store it in a temporary location.
    with urllib.request.urlopen(url) as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)

    # Get the HTTP status code that was sent with the response
    response_status_code = response.getcode()

    #
    if response_status_code == 200:
        # Open the temporary file containing the html page and read it
        with open(tmp_file.name) as html:
            page = html.read()

        # convert page into a string.
        page_string = str(page)
        # print("page_string: \n{0}".format(page_string))

        # Convert page result into a list
        list_of_proxies_ip = page_string.split()
        # print("list_of_proxies_ip: \n{0}".format(list_of_proxies_ip))

    return list_of_proxies_ip


def main():
    list_of_proxies_ip = get_list_of_http_proxies(URL_HTTP_PROXIES)
    # Print the list.
    if len(list_of_proxies_ip) > 0:
        print("\nList of proxy servers found ({0}):\n".format(len(list_of_proxies_ip)))
        for i in range(len(list_of_proxies_ip)):
            print("{0}".format(list_of_proxies_ip[i]))
    else:
        print("We couldn't find any server")


if __name__ == '__main__':
    main()

