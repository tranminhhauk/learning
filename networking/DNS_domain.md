# Overview of Domain and DNS

**Key Summary:**  domain is a name that helps people remember it easily, DNS is a system that translates that name into IP addresses so that computers can connect to each other.

## 1. Domain

-A domain name is a unique address on the Internet used to access a website, allowing devices and users to find the website.
    - Ex: google.com, portal.ut.edu
## Structure of Domain

-The structure of a domain name consists of strings of characters separated by dots, including: Website name, top level domain name, second level domain name

    -Top-Level Domain : ex: .com, .net, .org

    -Second-Level Domain: It is a proper name, usually located on the left top level domain, ex: facebook, google

    -Subdomain: located on the left second level domain, ex: www

    EX: https://www.facebook.com/

    TLD: .com
    SLD: facebook
    subdomain: wwww

## 2. What is DNS (Domain Name System) ?

**The Domain Name System (DNS)** is like the phone book of the Internet. People access information online through domains

**web browser** interactive with the IP address

**DNS** translates domain names into IP addresses so browsers can interactive with user 

## How does DNS work ?

DNS resolution include converting a hostname (ex www.facebook.com) to a computer-friendly IP address (ex 192.168.1.1)

For web browsers, DNS lookups occur "in the background" and do not request any interaction from the user's computer beyond the initial request. 
## Important types of servers DNS

-DNS Recursive Resolver: "Middleman" — receives a request from a client, automatically asks other servers until there is a response, then responds to the client

-Root server: Know which TLD and where it, usually it serves as a reference to more specific locations

-TLD server: This server is the next step in the process of finding a specific IP address, and it stores the last part of the domain name (For ex, in facebook.com, the server TLD is ".com").

-Authoritative Name Server: This is the final stop in the domain name server query process. If the authoritative domain name server has access to the requested record, it will return the IP address for the requested hostname to the DNS recursive server.

## DNS lookup process
DNS involves translating domain names into corresponding IP addresses

1. The user types "facebook.com" into the web browser, and this query is transmitted over the Internet and received by a DNS Recursive Resolver

2. The resolver then queries the DNS Root Name Server (.)

3. The Root Server responds to the resolver with the address of the Top-Level Domain (TLD) DNS Server (such as .com or .net), which stores information for its domains. When looking up facebook.com, our request is directed to the .com TLD.

4. The resolver then sends a request to the .com Top-Level Domain server

5. The TLD Server then responds with the IP address of the Authoritative Name Server responsible for facebook.com (not the IP of facebook.com itself)

6. Finally, the recursive resolver sends the query to the Authoritative Name Server

7. The IP address for facebook.com is then returned to the resolver by the Authoritative Name Server

8. The DNS resolver then responds to the web browser with the IP address of the domain originally requested

9. The browser requests HTTP to the IP address