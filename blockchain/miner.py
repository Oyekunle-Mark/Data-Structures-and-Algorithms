import hashlib
import requests

import sys
import json
from typing import NewType, Dict, Any

BlockType = NewType('BlockType', Dict[str, Any])


def proof_of_work(block: BlockType) -> int:
    """
    Simple Proof of Work Algorithm
    Stringify the block and look for a proof.
    Loop through possibilities, checking each one against `valid_proof`
    in an effort to find a number that is a valid proof
    :return: A valid proof for the provided block
    """
    block_string = json.dumps(block, sort_keys=True)
    proof = 0

    # loop while the return from a call to valid proof is False
    while valid_proof(block_string, proof) is False:
        proof += 1

    return proof


def valid_proof(block_string: str, proof: int) -> bool:
    """
    Validates the Proof:  Does hash(block_string, proof) contain 6
    leading zeroes?  Return true if the proof is valid
    :param block_string: <string> The stringified block to use to
    check in combination with `proof`
    :param proof: <int?> The value that when combined with the
    stringified previous block results in a hash that has the
    correct number of leading zeroes.
    :return: True if the resulting hash is a valid proof, False otherwise
    """
    guess = f"{block_string}{proof}".encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    return guess_hash[:6] == "000000"


if __name__ == '__main__':
    # What is the server address? IE `python3 miner.py https://server.com/api/`
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    # the coin count
    coins = 0

    # Load ID
    f = open("miner_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    # Run forever until interrupted
    while True:
        r = requests.get(url=node + "/last_block")

        # Handle non-json response
        try:
            data = r.json()
        except ValueError:
            print("Error:  Non-json response")
            print("Response returned:")
            print(r)
            break

        # TODO: Get the block from `data` and use it to look for a new proof
        last_block = data["last_block"]

        # print message to inform that miner is finding proof
        print("Finding proof...")
        new_proof = proof_of_work(last_block)
        # print message to inform that miner has found proof
        print("Proof found.")

        # When found, POST it to the server {"proof": new_proof, "id": id}
        post_data = {"proof": new_proof, "id": id}

        # send the proof to the blockchain server
        r = requests.post(url=node + "/mine", json=post_data)

        if r.status_code == 400:
            print("Post data to blockchain must contain proof and id")
            print(r)
            break

        # get the response from the server
        data = r.json()

        # TODO: If the server responds with a 'message' 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        if data["message"] == "New Block Forged":
            coins += 1
            print("New block forged")
        else:
            print(data["message"])

        # print the amount of coins
        print(f"You have {coins} coin[s]")
