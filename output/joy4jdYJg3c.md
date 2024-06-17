# Summary

### Summary of Technical Talk on Delta 4.0

**Introduction to Delta 4.0:**
- Delta 4.0 is introduced as the most significant update in Delta's history.
- The integration brings numerous new features, enhancing functionality and ease of use with diverse datasets.

**Key Features and Innovations:**

1. **Liquid Clustering:**
   - Intended to simplify the process of partitioning data.
   - Eliminates the complexities associated with over-partitioning and small files.
   - Introduces a novel data layout strategy.
   - Offers substantial performance improvements: up to 7x faster writes and 12x faster reads.
   - Eases schema evolution without the need for extensive data rewriting.
   - Already in use by approximately 1,500 customers, with significant success (e.g., Shell reported over an order of magnitude improvement in performance).

2. **Open Variant Data Type:**
   - Addresses the challenges of working with semi-structured and alternative data sources in the AI era.
   - Combines openness, flexibility, and performance.
   - Avoids compromises by enabling efficient storage and access to semi-structured data without proprietary limitations.
   - Achieves 8x faster performance compared to storing JSON data as raw strings.
   - The variant data type code is integrated into Apache Spark and made available as open source, promoting a non-proprietary, open format for semi-structured data storage.

**Overall Benefits of Delta 4.0:**
- The update emphasizes interoperability within the ecosystem.
- Provides remarkable performance benefits.
- Improves usability, making data management easier and more efficient.

**Conclusion:**
- Delta 4.0 offers a powerful, user-friendly update poised to enhance data handling and performance across various use cases, encouraging broader adoption and innovation.

**Thank You:**
- The talk concluded by acknowledging the advancements and expressing gratitude for the collaborative efforts in making Delta 4.0 a milestone release.

# Transcription

 That integration is super awesome. It's very exciting. OK, so how do we top that? By not going back, by going forward. And forward to Delta 4.0. So we have the branch cut. It's available. Delta 4.0 is the biggest change in Delta since history. It's jam-packed with new features and functionality, things like coordinated commits, collations, all sorts of new functionality that make it easier to work with various different types of data sets. We won't have time to go through all of this. I'm going to pick a couple and dive into why these are such amazing features. So liquid clustering is generally available now as part of Delta 4.0. And with liquid clustering, we really wanted to set out to solve this challenge that so many people have brought up. Partitioning, it's good for performance, but it's so complicated. You get over partitioning small files, you pick the wrong thing, it's a pain to resolve. And liquid solves this with a novel data layout strategy that's so easy to use that we hope all of you will say goodbye to partitions by. You never need to say that again when you define a table. Not only is it easy to use, we found out it is up to seven times faster for writes and 12x faster for reads. So the performance benefits are amazing. And of course, it's easy to evolve the schema, make changes, define anything without having to worry about all your data being rewritten and transformed. And there are about 1,500 people, customers, actively using this. The adoption has been insane. Over 1.2 zettabytes of data have been skipped. And you don't have to take my word for it. Even Shell, when they started using it for their time series workloads, saw over an order of magnitude improvement and performance. And it was just so easy to use. Next, open variant data type. And this one's really important. That first word, open, is really exciting. So what happens is now in this world of AI, you have more and more semi-structured text data, alternative data sources, all of this coming into the Lake House. And we wanted to come up with a way to make it easier for people to store and work with these types of data in Delta. And usually what happens is when you're stuck with semi-structured data, most of the data engineers, they sort of have to make a compromise. And none of us like to make compromises. But usually it's about being open, flexible, or fast. And often, they'd only be able to pick two out of these three. So for example, for semi-structured data, one approach is to store everything as a string. That's open. It gives you tons of flexibility. But parsing strings is slow. Why would you store a number as a string and have to reread it every time? So of course, there's an option to pick the fields out of your semi-structured data, make them concrete types, and you get amazing performance. This is open, very fast to access. However, if you have sparse data, you sort of lose out on a lot of that flexibility to modify the schema. And relational databases for a while have had special enum or variant data types. But all of those had always been proprietary. If you wanted to use them to get a balance of not having to store everything as a string and not having to shard out every single column, you got locked in. And so that's why we're very excited with Variant to be able to kind of get that sweet spot in the middle. You can have your JSON data store it with flexibility, fully open, with amazing performance. It's very easy to use. It works with even complex JSON. Here's an example of the syntax. And we found, of course, it's eight times faster than storing your JSON data as raw strings. This is just tremendous. So if you're storing JSON in a string field today, go back to work or home and start using Variant. It's available in DVR 15.3. But most importantly, all of the code for Variant is already checked in to Apache Spark. There's a common subdirectory in the 4.0 branch right now that has all of the implementation details for Variant and all of the operators. And there's a binary format code definition and library that we've made available open source so all the other data engines can also use Variant. We really want this to be an official open format that everyone adopts so that finally we have a non-proprietary way of storing semi-structured data reliably. And so with that, yeah. Oh, it's a big deal. With that, I just want to summarize Delta Lake 4.0. It's interoperable. We have this amazing ecosystem of people like Hannes working together, making it better and stronger. You get amazing performance benefits. And all of this is just so much easier to use now than it ever was before. Thank you.