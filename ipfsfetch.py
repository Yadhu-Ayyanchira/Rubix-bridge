import ipfshttpclient

# Specify the path to the swarm key file
swarm_key_path = "testswarm.key"  # Replace with the actual path


    # Connect to the IPFS node using the swarm key file
client = ipfshttpclient.connect('/tcp/0.0.0.0:5002', offline=1)

    # Now you can interact with the IPFS node as before
ipfs_hash = 'QmcdZQtRZjAD45PgRdCR54TAYKWWSkNTKdp5y8qMHkJDtu'
data = client.cat(ipfs_hash)

    # Assuming the data is a text file, you can decode it
decoded_data = data.decode('utf-8')

print("Retrieved data:")
print(decoded_data)

# except ipfshttpclient.exceptions.StatusError as e:
    # print(f"Error: {e}")

# Close the IPFS client connection
client.close()
