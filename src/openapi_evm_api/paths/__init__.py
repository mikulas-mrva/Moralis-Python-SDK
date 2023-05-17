# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_evm_api.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ADDRESS_NFT = "/{address}/nft"
    NFT_GET_MULTIPLE_NFTS = "/nft/getMultipleNFTs"
    ADDRESS_NFT_TRANSFERS = "/{address}/nft/transfers"
    ADDRESS_NFT_COLLECTIONS = "/{address}/nft/collections"
    NFT_ADDRESS = "/nft/{address}"
    NFT_ADDRESS_OWNERS = "/nft/{address}/owners"
    NFT_ADDRESS_TRANSFERS = "/nft/{address}/transfers"
    NFT_TRANSFERS = "/nft/transfers"
    BLOCK_BLOCK_NUMBER_OR_HASH_NFT_TRANSFERS = "/block/{block_number_or_hash}/nft/transfers"
    NFT_ADDRESS_TRADES = "/nft/{address}/trades"
    NFT_ADDRESS_METADATA = "/nft/{address}/metadata"
    NFT_ADDRESS_TOKEN_ID = "/nft/{address}/{token_id}"
    NFT_ADDRESS_TOKEN_ID_TRANSFERS = "/nft/{address}/{token_id}/transfers"
    NFT_ADDRESS_TOKEN_ID_OWNERS = "/nft/{address}/{token_id}/owners"
    NFT_ADDRESS_SYNC = "/nft/{address}/sync"
    NFT_ADDRESS_TOKEN_ID_METADATA_RESYNC = "/nft/{address}/{token_id}/metadata/resync"
    NFT_ADDRESS_LOWESTPRICE = "/nft/{address}/lowestprice"
    NFT_SEARCH = "/nft/search"
    ERC20_ADDRESS_PRICE = "/erc20/{address}/price"
    ADDRESS_ERC20 = "/{address}/erc20"
    ADDRESS_ERC20_TRANSFERS = "/{address}/erc20/transfers"
    ERC20_METADATA = "/erc20/metadata"
    ERC20_METADATA_SYMBOLS = "/erc20/metadata/symbols"
    ERC20_ADDRESS_ALLOWANCE = "/erc20/{address}/allowance"
    ERC20_ADDRESS_TRANSFERS = "/erc20/{address}/transfers"
    ERC20_TRANSFERS = "/erc20/transfers"
    ERC20_MINTS = "/erc20/mints"
    ERC20_BURNS = "/erc20/burns"
    ERC20_APPROVALS = "/erc20/approvals"
    ADDRESS_BALANCE = "/{address}/balance"
    WALLETS_BALANCES = "/wallets/balances"
    ADDRESS = "/{address}"
    ADDRESS_VERBOSE = "/{address}/verbose"
    TRANSACTION_TRANSACTION_HASH_INTERNALTRANSACTIONS = "/transaction/{transaction_hash}/internal-transactions"
    TRANSACTION_TRANSACTION_HASH = "/transaction/{transaction_hash}"
    TRANSACTION_TRANSACTION_HASH_VERBOSE = "/transaction/{transaction_hash}/verbose"
    BLOCK_BLOCK_NUMBER_OR_HASH = "/block/{block_number_or_hash}"
    DATE_TO_BLOCK = "/dateToBlock"
    ADDRESS_LOGS = "/{address}/logs"
    ADDRESS_EVENTS = "/{address}/events"
    ADDRESS_FUNCTION = "/{address}/function"
    WEB3_VERSION = "/web3/version"
    INFO_ENDPOINT_WEIGHTS = "/info/endpointWeights"
    RESOLVE_ADDRESS_REVERSE = "/resolve/{address}/reverse"
    RESOLVE_DOMAIN = "/resolve/{domain}"
    RESOLVE_ENS_DOMAIN = "/resolve/ens/{domain}"
    PAIR_ADDRESS_RESERVES = "/{pair_address}/reserves"
    TOKEN0_ADDRESS_TOKEN1_ADDRESS_PAIR_ADDRESS = "/{token0_address}/{token1_address}/pairAddress"
    IPFS_UPLOAD_FOLDER = "/ipfs/uploadFolder"
    MARKETDATA_ERC20S_TOPTOKENS = "/market-data/erc20s/top-tokens"
    MARKETDATA_ERC20S_TOPMOVERS = "/market-data/erc20s/top-movers"
    MARKETDATA_NFTS_TOPCOLLECTIONS = "/market-data/nfts/top-collections"
    MARKETDATA_NFTS_HOTTESTCOLLECTIONS = "/market-data/nfts/hottest-collections"
    CONTRACTSREVIEW = "/contracts-review"
