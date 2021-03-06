"""

/*
 *
 * Crypto.BI Toolbox
 * https://Crypto.BI/
 *
 * Author: José Fonseca (self, https://zefonseca.com/)
 *
 * Distributed under the MIT software license, see the accompanying
 * file COPYING or http://www.opensource.org/licenses/mit-license.php.
 *
 */

"""

class CBDAODriver:
    """
        Abstract class / interface for database access layer.
        Override all methods to create DB interface for other DBMS.
        All hash parameters are bytes instances.
    """
    def connect(self, user, password, host, db):
        pass

    def test_connection(self):
        pass

    def insert_block(self, block):
        pass

    def get_block_by_hash(self, hash):
        pass

    def get_next_block(self, prev_block_hash):
        pass

    def set_next_block_hash(self, thisblock_hash, nextblock_hash):
        pass

    def set_next_block_hash_and_height(self, thisblock_hash, nextblock_hash, height):
        pass

    def get_latest_block(self):
        pass

    def get_latest_block_hash(self):
        pass

    def insert_block_file(self, filename, hash, byte_offset):
        pass

    def get_latest_block_file(self, filename, hash, byte_offset):
        pass

    def insert_tx(self, tx):
        pass

    def list_tx_by_block(self, block_hash):
        pass

    def get_tx_by_hash(self, hash):
        pass

    def get_latest_tx(self):
        pass

    def insert_tx_in(self, tx):
        pass

    def get_tx_in(self, vin):
        pass

    def get_latest_tx_in(self):
        pass

    def list_tx_in(self, tx_hash):
        pass

    def insert_tx_out(self, tx):
        pass

    def get_tx_out(self, vout):
        pass

    def get_tx_out_byhash_nvout(self, txhash, nvout):
        pass

    def get_latest_tx_out(self):
        pass

    def list_tx_out(self, tx_hash):
        pass

    def list_tx_out_from_inputs(self, input_list):
        pass

    def insert_tx_out_address(self, tx_hash, nvout, addr, req_sigs, script_type):
        pass

    def list_tx_out_addresses(self, tx_hash):
        pass

    def get_tx_out_address_byhash_nvout(self, txhash, nvout):
        pass

    def insert_address_graph(self, ag):
        pass

    def list_address_graph(self, addr):
        pass

    def set_address_balance(self, address, satoshis):
        pass

    def get_address_balance(self, address):
        pass

    def insert_info_node(self, inode):
        pass

    def get_info_node_by_id(self, id):
        pass

    def list_info_node_by_address(self, address):
        pass

    def list_info_node_by_block_hash(self, hash):
        pass

    def list_info_node_by_tx_hash(self, hash):
        pass

    def list_info_nodes(self):
        pass

    def search_info_node(self, q):
        pass

    def update_info_node(self, inode):
        pass

    def delete_info_node(self, id):
        pass

    def disable_keys(self):
        pass

    def enable_keys(self):
        pass

    def list_tables(self):
        pass
