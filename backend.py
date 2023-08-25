import requests
#Dummy Class for 
class name{
    int quant;
    int price;
}
List<name> bids = new ArrayList<>();
List<name> asks = new ArrayList<>();

Gemini Data
for data in GeminiData{
    if(data.price ){
        Name name = new Name();
        name.price = data.price
        name.qua = 
        bids.add(name);
    }
}

#Should Contain Quantity and Price as the Parameters
#Dummy Class for bids

def fetch_order_book(exchange_url):
    response = requests.get(exchange_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch order book from:", exchange_url)
        return None

def accumulate_orders(orders, threshold):
    accumulated = []
    total_amount = 0.0
    for order in orders:
        amount = float(order['amount'])
        if total_amount + amount < threshold:
            accumulated.append(order)
            total_amount += amount
        while #condition(total_amount + amount >= threshold):
            #Sliding window Approach
        else:
            remaining_amount = threshold - total_amount
            fraction = remaining_amount / amount
            partial_order = order.copy()
            #Need Quantity in the partial order
            partial_order['amount'] = str(remaining_amount)
            accumulated.append(partial_order)
            #increment the left pointers
            break
        #Final List should contain quantity and amount values
        #Use Dummy Class
    return accumulated

def merge_order_books(order_books):
    merged_bids = []
    merged_asks = []
    #bids and asks contain items of dictionary
    #each dictionary item contain keys as quantity and price

    for order_book in order_books:
        bids = order_book.get("bids", [])
        asks = order_book.get("asks", [])
        
        merged_bids.extend(bids)
        merged_asks.extend(asks)

        #Need quantity along with price

        merged_bids.sort(key=lambda x: float(x['price']), reverse=True)
        merged_asks.sort(key=lambda x: float(x['price']))

        threshold = 10.0

        accumulated_bids = accumulate_orders(merged_bids, threshold)
        accumulated_asks = accumulate_orders(merged_asks, threshold)


    return accumulated_bids, accumulated_asks

def gemini_adapt_order_books(order_book):
    #Code to adapt the Gemini Exchange data to Locally Declared Classes
    #Use Dummy Class
    #for loop to adapt data

def kraken_adapt_order_books(order_book):
    #Code to adapt the Kranken Exchange data to Locally Declared Classes
    #Use Dummy Class
    #for loop to adapt data

if __name__ == "__main__":
    kraken_order_book_url = "https://api.kraken.com/0/public/Depth?pair=XBTUSD"
    gemini_order_book_url = "https://api.gemini.com/v1/book/BTCUSD"
    
    kraken_order_book = fetch_order_book(kraken_order_book_url)
    gemini_order_book = fetch_order_book(gemini_order_book_url)
    
    if kraken_order_book and gemini_order_book:
        order_books = [kraken_order_book, gemini_order_book]
        #Call the adapt order books # input the exchange book and output the local data
        #Then add the returned local ordered books
        merged_bids, merged_asks = merge_order_books(order_books)
        try:
            buy_price = float(merged_asks[0]['price'])  # Get the 'price' value from the dictionary
            sell_price = float(merged_bids[0]['price'])  # Get the 'price' value from the dictionary

            print("Price to buy 10 bitcoins: ", buy_price)
            print("Price to sell 10 bitcoins: ", sell_price)
        except IndexError:
            print("Order book is empty.")
    else:
        print("Failed to fetch order books from at least one exchange.")