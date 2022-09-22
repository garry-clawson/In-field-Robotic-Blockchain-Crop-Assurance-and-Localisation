pragma solidity >=0.4.22 <0.9.0;

// contracts/ImageStore.sol

contract ImageStore {
    string[] private list;

    // Emitted when the stored a new item is added to the list
    event ItemAdded(string item);

    // Adds a new item in the list
    function addItem(string memory newItem) public {
        list.push(newItem);
        emit ItemAdded(newItem);
    }

    // Gets the item from the list according to index
    function getListItem(uint256 index)
        public
        view
        returns (string memory item)
    {
        return list[index];
    }
    
    // Gets the size of the list
    function getListSize() public view returns (uint256 size) {
        return list.length;
    }
}