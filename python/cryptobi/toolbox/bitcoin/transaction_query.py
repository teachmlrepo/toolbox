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

# KNOWN BUG: must load the mysql module before all other libraries
# so they don't load an incompatible version of openssl which causes
# random segfaults with mysql procedures
# mysql module is not used here but must be loaded first on some systems
from mysql import connector

import sys
from cryptobi.toolbox.system.CBConfig import CBConfig
from cryptobi.db.dao.CBDAO import CBDAO
import argparse

parser = argparse.ArgumentParser(description = "Query a Bitcoin TX from the local databse.")
parser.add_argument('tx_hash', type=str, nargs=1)
args = parser.parse_args()

config = CBConfig.get_config()

dao_a = CBDAO()
dao = dao_a.get_DAO()

tx_hash = config.get_conf("listargs")

if not len(tx_hash) > 0:
    config.log_error("Invalid TX hash.")
    sys.exit(1)

tx = dao.get_tx_by_hash(bytes.fromhex(tx_hash))
print(tx)

