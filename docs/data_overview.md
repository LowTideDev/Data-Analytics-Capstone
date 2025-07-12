# Data Overview

The CSV files share the following columns:

1. `AppID` – Steam application ID
2. `Name` – Game title
3. `Release date` – Date of release
4. `Estimated owners` – Range string indicating estimated ownership
5. `Peak CCU` – Highest concurrent users recorded
6. `Required age` – Age requirement
7. `Price` – Full price in USD
8. `DiscountDLC count` – Number of DLC items or discount info
9. `About the game` – Full description text
10. `Supported languages`
11. `Full audio languages`
12. `Reviews` – Overview of user reviews
13. `Header image` – Image URL
14. `Website` – Official website
15. `Support url`
16. `Support email`
17. `Windows` – Y/N flag
18. `Mac` – Y/N flag
19. `Linux` – Y/N flag
20. `Metacritic score`
21. `Metacritic url`
22. `User score`
23. `Positive` – Count of positive reviews
24. `Negative` – Count of negative reviews
25. `Score rank` – SteamDB ranking
26. `Achievements` – Number of achievements
27. `Recommendations` – Steam recommendations
28. `Notes`
29. `Average playtime forever`
30. `Average playtime two weeks`
31. `Median playtime forever`
32. `Median playtime two weeks`
33. `Developers`
34. `Publishers`
35. `Categories`
36. `Genres`
37. `Tags`
38. `Screenshots`
39. `Movies`

The JSON files contain similar information but keyed by `AppID`. After combining them in memory, you will have a comprehensive dataset that can be analyzed using your preferred tools without creating a giant file in the repo.
