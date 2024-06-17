# Summary

In the technical talk led by Ali, key updates and innovations around Delta Lake and its new feature, Delta Lake Uniform, were discussed. Here are the highlighted points:

1. **Delta Lake Uniform GA Announcement**: The general availability of Delta Lake Uniform, designed for lakehouse format interoperability, was officially announced. This feature enables data written in one format (Delta) to be read as another (Iceberg, Hootie), promoting flexibility and reducing duplication.

2. **Interoperability and Collaboration**: Collaborations with Apache X Table and Hootie teams have enabled smooth interoperability, with ongoing efforts with the Iceberg team to improve the system further.

3. **Performance and Features**: Uniform maintains impressive performance with minimal overhead and supports various data types, a production-ready catalog, and the Iceberg REST catalog API.

4. **Adoption and Scale**: Over four exabytes of data have been loaded through Uniform, with widespread adoption by hundreds of customers, including M-Science. The overall Delta Lake adoption is substantial, processing over nine exabytes and being used extensively across Fortune 500 companies.

5. **Community Contributions**: A significant portion (66%) of contributions to Delta Lake come from outside Databricks, driven by a vibrant developer community.

6. **Innovative Features**: Recent features include change data feed, deletion vectors for faster updates, row IDs, and law compaction, beneficial for workloads involving frequent data operations.

7. **Delta Kernel and Ecosystem Integration**: The introduction of Delta Kernel facilitates easier integration of Delta formats into applications. Enhanced connectors such as the Trino rust connector further improve usability.

8. **New Integrations**: Delta has gained support from major platforms like Google's BigQuery and DuckDB. Hannes from DuckDB, a co-creator, is introduced to discuss Delta integration into DuckDB.

These points highlight Delta Lake's role in streamlining data management, its collaborative ecosystem, and constant enhancements catering to modern data requirements.

# Transcription

 Thanks, Ali. And a lot of us, we used to work together with Ryan in the past, and it's really exciting to have him here, so we could work together again. So this talk's going to be very exciting. Delta Lake. First of all, can announce the general availability of Delta Lake Uniform. What is Uniform? Really, it's just short for two words, universal format. It's our approach to allow full lakehouse format interoperability. See, with all of these different formats, Delta, Iceberg, Hootie, it's essentially a collection of data files in Parquet and a little bit of metadata on the side. All of the formats use the same MVCC transactional techniques to keep that together. And so we thought to ourselves, in this age of LLMs, transforming language left and right, couldn't we just find a way to translate that metadata into different formats so that you just need to have one copy? And that's exactly what we're doing with Uniform. The Uniform GA allows you to essentially write data as Delta and be able to read it as Iceberg, Hootie. And we've worked very closely with the Apache X Table and Hootie team to make that possible. And we're going to be working with the Iceberg team to make that even better. The great thing about Uniform is there's barely a noticeable performance overhead. It's super fast. You get awesome features like liquid clustering. There's support for all of the different data types from map, lists, arrays. And best of all, it's got a production-ready catalog. With UC and Uniform, it's one of the only live implementations of the Iceberg REST catalog API. And that's available for everybody using Uniform. There have been over four exabytes of data that have already been loaded through Uniform. We have hundreds of customers using it. And one of them, in particular, M-Science, as you can see here, was very happy that they were able to have one copy of their data, which allowed them to reduce costs and have better time to value. And it's innovations like Uniform that are really making Delta Lake the most adopted open lakehouse format. There have been over nine exabytes of data processed on Delta yesterday, over a billion clusters per year using it. And this is tremendous growth. It's 2x more than last year. And if you're like me, and when you saw these numbers, I did not believe nine exabytes. I had literally up till yesterday, we were going back, looking at the code, making sure they calculated correctly. Because it's just a tremendous amount of data every day that's going into Delta. And it's adopted by a large percentage of the fortune, 500, 10,000 plus companies in production, lots of new features. But most interestingly, it's sort of that last number. There are over 500 contributors. And best of all, according to the Linux Foundation, and this is their project analytics site, it's open, anyone can go to it today, over about 66% of contributions to Delta come from companies outside of Databricks. And it's this community that just really makes us super excited and enables a ton of these features that are now available. And these are time-tested, awesome, innovative functionality, things like change data feed, law compaction. I love the row IDs feature that just came out. But there are things like deletion vectors. Deletion vectors are a way that allow you to do fast updates and DML to your data. In many cases, it's 10 times faster than merge, used to be. So if you have a DBT workloads or you're doing lots of operational changes to data, deletion vectors make your life easier. And there have been over 100 trillion row rewrites that have been saved because of these deletion vector features. And it's enabled by default for all Databricks users. And so it's through these features that we've also been able to unlock access to this amazing ecosystem of tools that support Delta. And with Uniform, that's now GA, we're able to get the same access to the hoodie and iceberg ecosystem. So if you have tools and SDKs, applications that work in there, they're all part of the Delta family now, thanks to Uniform. And there's been some great improvements to a lot of the connectors, the Trino rust connector, lots of awesome innovation happening here. And a lot of that is thanks to this new thing that we've developed called Delta Kernel. Essentially, at the core of all of this, there's a small library that you can just plug and play into your applications or SDKs that contains all the logic for the Delta formats, all the version changes, new features, and it's making it so much easier for people to integrate and adopt Delta. And most importantly, stay up to date with the latest features. And we've been seeing this, the Delta Rust connector is community supported and has amazing traction. Just a few weeks ago at Google's IO conference, I believe they BigQuery introduced complete support for Delta. And very recently, DuckDB added full support for Delta. And best part of this is we have Hannes here, who's the co-founder, one of the co-creators of DuckDB, CEO of DuckDB Labs, professor of computer science, who's going to talk to us a little bit about how they integrated Delta into DuckDB. Hannes, get over here.