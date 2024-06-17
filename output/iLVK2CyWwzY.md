# Summary

### Summary of Technical Talk on Databricks Clean Rooms

**Main Announcement:**
- Databricks is launching a public preview of their new feature, Databricks Clean Rooms, later this summer. Clean rooms enable private computations and collaboration between parties while maintaining data privacy.

**Key Features and Benefits:**
1. **Private Computation:**
   - Parties can bring various data assets (tables, code, AI models, unstructured data) into the clean room.
   - Computation results can be shared with one recipient without exposing the underlying data.

2. **Versatile Computation Capabilities:**
   - Supports a wide array of computations including machine learning, SQL, Python, R, etc., unlike other solutions that might only support SQL.

3. **Integration with Delta Sharing and Lakehouse Federation:**
   - Facilitates cross-cloud and cross-platform collaboration.
   - Supports seamless connections to primary data stores not on Databricks, ensuring wide compatibility.

**Use Case Highlight:**
- Mastercard is exploring various use cases involving private algorithms and techniques, showcasing the feature's utility.

**Demonstration Walkthrough:**
1. **Retailer and Supplier Collaboration Scenario:**
   - **Objective:** A retailer and supplier need to run a joint ad campaign, requiring collaborative analysis of customer data without sharing sensitive information.
   - **Challenges:** Data on different clouds/regions, sharing sensitive information, and using machine learning and Python.

2. **Steps in Databricks Clean Room:**
   a. Retailer (on Azure, East US):
      - Creates a clean room and specifies the supplier as a collaborator.
      - Brings in structured data (audience graph table) and unstructured data/AI models for audience segmentation.
      - Adds a Python-based notebook for machine learning.
   b. Supplier:
      - Joins clean room (on Snowflake, outside Databricks) without custom ETL pipeline.
      - Brings in their customer data using Lakehouse federated tables.
      - Runs the pre-configured notebook, resulting in visual insights, identifying 1.2 million target households.

**Conclusion:**
- The presentation highlighted that Databricks Clean Rooms enable secure, cross-platform, and cross-cloud data collaboration.
- Emphasis on governance and open, cross-platform approaches as essentials for the future.
- Encouragement for users to join Databricks' open ecosystem to leverage these innovative solutions.
  
This new feature aims to revolutionize how industries collaborate on data and AI securely and efficiently.

# Transcription

 The final thing I want to talk about is that we're soon launching public preview of Databricks clean rooms clean rooms are a way to do a private computation with with another party where you can each bring in your assets you can bring in some tables some Codes some unstructured data some AI models any kind of asset you can have on the Databricks platform And you can agree on a computation with someone else that you run and then send the results to just one recipient So for example, it could be as simple as you each have some tables and you want to figure out You know how many records you both have in common and it can be as complicated as you know Someone has a machine learning model. They want to keep private someone has a data set They want to keep private but they want to apply these two together and get the predictions or get the differences between their two models So two things really distinguish Databricks clean rooms from other clean room solutions out there The first is because you have this complete data and AI platform you can really run any computation It can be machine learning sequel Python R and so on versus just sequel in in many other clean room solutions And also Databricks clean rooms is built on Delta sharing it integrates with Lakehouse Federation So it's very easy to do cross-cloud and even cross platform collaboration If someone's primary data store is not Databricks They can still seamlessly connected to the clean room and do work on that So this is going to go in into public preview Just a little bit later this summer and we've already seen some really awesome use cases one Company we've been working closely with is Mastercard who has so so many exciting use cases with a whole range of different partners You can imagine, you know the different kinds of things that they they can do with their data and who is You know looking for the best way to do private versions of the state-of-the-art Algorithms and techniques to work with this data So I want to show you all this collaboration work in action and for that we have our third demo I'd like to invite Darshan who is our product manager for clean homes Thanks Matei Picture this I'm part of a media team at a large retailer We are teaming up with a supplier to run a joint advertisement campaign to grow our sales For this we need to identify our target audience We need to collaborate on joint customer data I As a retailer have data on my customers and their shopping behavior My supplier has their customer loyalty data However, we have some challenges First we cannot share any sensitive information about our customers with each other second our data is on different clouds regions and data platforms and Finally, we want to leverage machine learning and Python for our analysis and not just sequel Databricks clean rooms can help with all of this in a privacy safe environment Let's see how So here I am on the Databricks clean room console as the retailer and I create a clean room in a few simple steps I'm using Azure and East US to as my cloud and region and what's amazing is that it doesn't matter that my supplier And I are on different regions and clouds. I Then go ahead and specify my supplier as a collaborator and Once the clean room is created I bring in the data I Add my audience graph table and what's awesome is that I can also bring in unstructured data and AI models to collaborate with and here I go ahead and add an ad science private library that I've created that invokes an AI function to help me with my audience segmentation task So now it's time to add a notebook and I add one I've pre-created for audience segmentation That I've pre-configured to use my private library and the best part about this notebook I can use Python for machine learning Now my clean room is ready for my supplier to come join so let me flip hats I'm now the supplier hence dark mode and I joined the clean room that my retail counterpart added me to I See all the assets that they brought to the clean room and When I click into the audience graph table, I see the metadata associated with the table, but not the actual data This is perfect context for good collaboration while ensuring that I'm not privy to any sensitive information Now it's my turn to bring in my customer data But my customer data is on a snowflake warehouse outside data bricks And I don't want to create a custom ETL pipeline to bring this data in and I don't have to because lucky for me I Can directly specify Lakehouse federated tables as sources to this clean room With no copy no ETL these clean rooms truly scale for cross-platform collaboration And now my favorite part I inspect the notebook the code looks good and I run it So the job run has successfully started And In a few seconds it's done and I'm presented with Delightful visual results to help me understand that we can target 1.2 million households for our campaign Based on factors such as customer age income bracket and household size So let's go back to our slides to summarize what we just saw Our retailer and supplier were able to bring their respective customer data to a privacy safe environment The clean room and collaborate without sharing any sensitive information with each other It didn't matter that they were in different clouds regions or data platforms They could collaborate on more than just structured data and they were able to use Python for machine learning Thank you all so much and back to you mate Awesome demo Yeah, so super excited about clean rooms and especially Cross-platform clean rooms. I think it's really going to transform a lot of industries It just makes sense to be able to collaborate on data and AI in real time in a secure fashion So I think overall I've given you a good sense of our approach. We really believe that picking, you know, the right Governance and and sharing foundation You know for your company is essential for the future and we think it it needs to be an open and cross-platform approach We've been thrilled to see both unity catalog and Delta sharing, you know Go from just an idea to being you know used, you know virtually all our customers in a few years and We're excited that both of these are open We're excited about the partners and we invite you to join the open ecosystem