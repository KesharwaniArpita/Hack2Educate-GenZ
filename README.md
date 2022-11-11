# Hack2Educate-GenZ

# Team GenZ
### The Team Members of GenZ are:
   - Harsh Raj
   - Raj Vardhan Tomar
   - Arpita Kesharwani
   - Rahul Kumar Mishra

## Theme we are workin on is ML / AI challenge
   - We will be given a Youtube video:
       - Determine if it is an educational video or not.
       - Determine which category or subcategory of BE would it belong to.
   - Accuracy: 90%+ on a custom dataset that will be provided after proof of concept.
   - Should be able to run in near-real-time on a server.
   
### Problem solving approach 
- We will try to solve this problem using Natural Language Programming. We will take the data of some YouTube channels to make the dataset and extract their title and description. Then the punctuations, emoji, etc. are removed from the extracted words. These words are then classified as educational and non-educational keywords. Then we will import the video to be checked and extract its title and description. Then we will remove the punctuations, emoji and the non-educational keywords. From the remaining words we will check how many words are educational and calculate the percentage of educational words. If this percentage is above a particular limit (where the accuracy is maximum) we will declare the video is educational. 

### Final Demo:
- The final demo will be website where one can paste the link of any YouTube video and know whether the content is educational or not. We will also try to make a chrome extension that will identify the video while it is being loaded and block the video if it is non educational. 

### Index
 - Project 1
   - We have learned how to use Application programming interface (API) to extract some data of YouTube Channels and Videos
     - We extracted data of some Educational, Entertainment, Tech and motivational Channels
  - Creating Dataset
   - We had created a dataset of title and description of approx 1.5 Lakh YouTube Videos from 45 different YouTube channels 
     - Now we are finding keywords from this data to create two different lists of Educational and Non-Educational words so that we can comment weather a video is for educational purpose otr not.
