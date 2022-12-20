import ssl
import socket

def verify_ssl_certificate(hostname):
    # Create a default SSL context
    context = ssl.create_default_context()

    try:
        # Create an SSL socket using the context and the target hostname
        s = context.wrap_socket(socket.socket(), server_hostname=hostname)
        # Connect to the target hostname on port 443
        s.connect((hostname, 443))
        # Get the peer certificate
        certificate = s.getpeercert()
        # If the connection and certificate are valid, print a message and return True
        print("SSL certificate for {} is valid.".format(hostname))
        return True
    except ssl.SSLError as e:
        # If there's an SSL error, print an error message and return False
        print("SSL certificate for {} is not valid: {}".format(hostname, e))
        return False

# Verify the SSL certificate for the target hostname
verify_ssl_certificate("example.com")
