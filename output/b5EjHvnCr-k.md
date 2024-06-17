# Summary

The technical talk provides an overview of the company's focus and recent developments. Key points include:

1. **Company Introduction**: 
   - The company is a public benefit corporation focused on code-first data science and has been around for 15 years.
   - They prioritize long-term development, particularly in open-source tools.

2. **Support and Tools**: 
   - They support hundreds of R packages and the RStudio IDE.
   - Over the past five years, they've expanded capabilities in the Python ecosystem with projects like Quarto, Shiny for Python, and GreatTables.

3. **SparklyR Package**:
   - In 2016, they developed SparklyR to provide an R implementation aligned with the tidyverse philosophy.
   - Spark Connect, introduced last year, solved the issue of running RStudio and R on servers, allowing direct client access.

4. **Collaborations and Integrations**:
   - They've collaborated with Databricks to support Spark Connect, Unity Catalog, and R user-defined functions.
   - This integration allows R users to leverage Spark effectively and collaborate within the Spark ecosystem.

5. **Developments and Products**:
   - Enhanced user accessibility with a simple one-line change to connect to Spark Connect from the desktop IDE.
   - Posit Workbench, their commercial product, supports RStudio, Jupyter Notebook, JupyterLab, and VS Code, integrating with Databricks' governance.

6. **Future Plans**:
   - Continued development of commercial products and open-source tools with deeper integrations with the Databricks stack.

7. **Call to Action**:
   - Encourages feedback from users trying out their new integrations and products.
   - Provides links for further information on collaborations with Spark and Databricks.

This summary highlights the company's dedication to open-source data science, key projects and tools, successful collaborations, and their plans for future product development.

# Transcription

 Good morning, everyone. Thank you very much for the introduction. It's very kind of you. I'm very excited to be here, and thank you, Databricks, for giving us the opportunity to speak to this audience. We, as a company, are probably some people that you don't know. You've never heard of us until he gave you a little bit of update. But we are a public benefit corporation. We've been around for about 15 years. Our focus is very much about code first data science. Our governance structure is one that allows us to think about things for a very, very long term. So our ambitions are actually to be around for the long haul to continue to invest in these open source tools. We support hundreds of R packages, and we also support the RStudio IDE. And if you've been watching us for a while, you may have noticed that over the last five years, we've added a lot of capabilities to the Python ecosystem. In some cases, these are multilingual solutions. So things like Quarto, Shiny for Python, GreatTables, all of these are examples of projects that we have. And we have more that are coming out over the coming years. Sorry, I'm having a hard time reading this slide. In 2016, we released a package called Sparkly R. And the reason we released it is because we wanted to have an idiomatic implementation for the R users that is more aligned with what the tidyverse is. And for those of you who don't know what the tidyverse is, it's like a philosophy of how you write packages and the patterns that sort of go along with that. The original design of Spark made it so that for users in corporations in particular to be able to use it, they would have to run RStudio and R on the servers themselves. And so you can imagine when Spark Connect became available last year, we were very, very excited. Because it finally solved one of the key problems that we saw, which is how do you make it so that the end user through a client does not have to get into a JVM and can just access it directly? And so happy to say, we started last year and basically by the end of last year, we had gotten support for Spark Connect to happen, Unity Catalog. We worked with the Databricks team to figure out how to make sure that Sparkly R and the IDE had clean support for that. And one of the most interesting things is we added support for R user-defined functions, which is actually a really big deal. Because now the R users in your organizations can actually participate in using Spark to solve the really hard problems. And they can collaborate with other people in the Spark ecosystem. So we're very excited about that. And we're interested in getting people's feedback on that if you get a chance to try it out. So this is very anticlimactic. For those of you who were there yesterday for the demo, you saw Casey, she's like, the world stopped. We decided to make Life Easy. It's hard to demo some of these things. But the change, this is the open source desktop IDE. And you can see that it's this one line change that you have to make to be able to connect to Spark Connect. And now this user on the desktop can go ahead and access the Spark cluster and leverage the full capabilities of that. This is one of the key things that we think that we can make a big difference in terms of people's ability to contribute and adopt Spark. So you probably have noticed, over the last year, we've been announcing all kinds of things with Databricks. One of the key things, obviously, where Sparkly are, and Spark Connect and support for that. But we have also been making changes on our commercial product. So the first commercial product that we have supporting this is something called Posit Workbench, which gives you a server-based, authoring environment that supports RStudio, Jupyter Notebook, JupyterLab, VS Code, and ties into the authentication and authorization of those systems. And so you basically get the full power of the governance that you have in Databricks, but having it surface to the data scientists. You can expect that over the coming year, you'll be more commercial products and open source tools that will have those tighter, tighter integrations with the Databricks stack. If you're at all curious or interested, feel free to check out any of these links to learn about how we're working more with Spark and Spark Connect and how we're working with Databricks. Thank you very much. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. [? ?]. ?]. [? ?]. ?]. ? ?