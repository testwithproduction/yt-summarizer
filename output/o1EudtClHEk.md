# Summary

In this technical talk, we discussed various features and functionalities of Databricks' Unity Catalog and Lakehouse Federation:

1. **Catalog Explorer**:
   - Provides a unified interface for browsing, applying access controls, and querying tables.
   - Supports navigation and organization of catalogs, tables, functions, models, volumes, and more, both within and outside of Databricks.
   
2. **Lakehouse Federation**:
   - Facilitates access to data systems like BigQuery, Glue, Hive, MySQL, Postgres, Redshift, Snowflake, and Azure SQL with simplified and secured access control.

3. **SQL Editor**:
   - Demonstrates querying external systems by joining federated Snowflake tables with Lakehouse native sources.
   - Integration of tables into Unity Catalog, which manages table management challenges such as automatic data layout, performance, and predictive optimizations.
   - Open API for accessing Unity Catalog objects externally.

4. **External Access and DuckDB Integration**:
   - Shows how to enable external access for Unity Catalog tables.
   - Example with DuckDB to query newly created objects demonstrates Databricks' commitment to open-source interoperability.

5. **Governance and Policy Enforcement**:
   - Demonstrates scalable governance using tags and attribute-based access control (A-BAC) policies combined with proactive PII (Personally Identifiable Information) monitoring.
   - Features simplified and proactive PII anomaly detection.
   - Example of creating a rule for masking email columns across all tables illustrates policy enforcement.

6. **Lakehouse Monitoring**:
   - Use of monitoring to detect and address PII in data and models.
   - Example of applying a mask to a user input column with detected PII.

The talk highlights Unity Catalog’s ability to seamlessly provide open access to data and enforce unified governance to ensure data integrity and security across diverse data and AI assets.

# Transcription

 Let's start with the catalog explorer on the left-hand side. This offers a unified interface for browsing, applying access controls, and querying tables. It enables you to navigate and organize catalogs, tables, functions, models, volumes, and other data systems both within and outside of Databricks. In some cases, only some of your data will reside in the Lakehouse. To address this, we've simplified and secured access control to systems such as BigQuery, catalogs such as Glue and Hive, MySQL, Postgres, Redshift, Snowflake, and Azure SQL. All of this is powered by Lakehouse Federation. Switching over here on the left-hand side to a SQL editor, I'll show you how to query an external data system by running some SQL that will join a store report table that is federated from Snowflake along with a Lakehouse native source that contains data on retail store returns. Once this table is created, this store report table will become a Unity Catalog managed object, which means the platform now handles all of your table management challenges, including automatic data layout, automatic performance, and predictive optimizations for you. But managed doesn't mean locked in. This table, or any Unity Catalog object, is accessible outside of Databricks via Unity Catalog's open API. Let me show you how easy it is to query this newly created object using DuckDB. First, I will opt this table in for external access as I've done for other tables in this catalog. Next, I'll switch over to DuckDB, which is the same nightly bill that you can access right now. I'll attach this catalog, Accounting Prod, to DuckDB. And now I'll run a quick query to see all of the tables in this catalog. All right. And as you can see, that store report table that I just created is right there. Next, I'll run a quick query to select from this table. I can do the same tables created in Unity Catalog and quickly query them using DuckDB's native Delta Reader. This is Databricks' commitment to open source and open interoperability here and now. So far, I've walked through Unity Catalog's Explorer, Lakehouse Federation, and our new open API. However, a major challenge for many organizations is ensuring consistent and scalable policy enforcement across a diverse range of data and AI assets. Let me show you how easy it is to scale your governance using tags and A-back policies combined with proactive PII monitoring. Let's switch over here to the online sales prod catalog and let's take a look at this table called Web Logs. One of the features that's been enabled in Unity Catalog is Lakehouse monitoring, which allows for simplified and proactive PII detection of anomalies in your data and models. On the left-hand side, you can explore columns and rows and you can see that PII has been detected in the user input column. This is obviously a problem. Before this data set can be used, this data must be masked and appropriate policies must be applied. Let's switch back to the catalog Explorer. Back in this Explorer, a new rule can be created to express policy across all data. It's now so much easier to mask all email columns across all tables of the single rule. Let's give this rule a name. Let's call it Mask Email. We're going to give it a quick description. Let's mask some emails. We want to apply this to all account users. This is a rule type of column mask. We're going to select a column mask function that I previously created, conveniently called Mask Email. We want to match on a condition when a column is detected that has a tag with a tag value of PII email. Let's go ahead and create that rule. That's it. Now, to validate this mask, we're going to go back to the Web Log Sales table. We can observe here in this table in the sample data, the user input column over here to the right that the data has now been masked. Since this applies to the entire catalog, let's go to a different table. Somewhere in here. There we go. As you can see, we've got an email address column in here as well, tagged PII email. Let's go up to sample data. As you can see over here as well, this table has also been masked with one rule. So, Matei, I've shown how Unity Catalog enables organizations to have open access to their data seamlessly, no matter where it resides while applying unified governance to ensure its integrity and security. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you.