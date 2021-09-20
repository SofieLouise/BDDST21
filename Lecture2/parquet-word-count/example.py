from hdfs import InsecureClient
from collections import Counter
import pyarrow.parquet as pq
import pandas as pd
import pyarrow as pa

client = InsecureClient('http://namenode:9870', user='root')

# Make wordcount reachable outside of the with-statement
wordcount = None

with client.read('/alice.txt', encoding='utf-8') as reader:
    wordcount = Counter(reader.read().split()).most_common(10)
    # Create a AvroWriter instance with the client and file name
    words = []
    counts = []

    for wordEntry in wordcount:
        words.append(wordEntry[0])
        counts.append(wordEntry[1])

    df = pd.DataFrame({
        'one': words,
        'two': counts})

    table = pa.Table.from_pandas(df)

    # Save the wordcount in a Parquet file and read it again!
    parquet_file = df.to_parquet()
    client.write('/word_count.parquet', parquet_file, overwrite=True)

with client.read('/word_count.parquet') as reader, open('local-parquet.parquet', 'w') as writer:
    content = reader.read()
    print(content)
    
# TODO somehow transform content to pandas
#table2 = pq.read_table(content)

#table2.to_pandas()