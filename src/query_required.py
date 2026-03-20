def scrappers_query(start_date, end_date,channel):
    query = f"""
    SELECT
        "batchId" as "Batch ID",
        count(*) AS "Total Scrapped Data",
        min("createdAt") AS "Batch Start Time",
        max("createdAt") AS "Batch End Time"
    FROM
        "{channel}ProductMerchant"
    WHERE
        "createdAt" >= '{start_date}' AND
        "createdAt" <= '{end_date}'
    GROUP BY
        "batchId"
    """
    print(f"Generated SQL Query for {channel}:\n{query}\n")
    return query