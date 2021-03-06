"""

/*
 *
 * Crypto.BI Toolbox
 * https://Crypto.BI/
 *
 * Author: José Fonseca (https://zefonseca.com/)
 *
 * Distributed under the MIT software license, see the accompanying
 * file COPYING or http://www.opensource.org/licenses/mit-license.php.
 *
 */

"""

class CBInfoNode:

    def __init__(self, cin_id, block_hash, tx_hash, address, content):
        self.cin_id = cin_id
        self.block_hash = block_hash
        self.tx_hash = tx_hash
        self.address = address
        self.content = content