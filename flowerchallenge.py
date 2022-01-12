data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for plants in data: # The new tables of flowers and shrubs are being added to,
    # from the temporary table plants created from data.
    if "Flower" in plants: # If the string is within the temporary table then everything with that string is added.
        flowers.append(plants)
    elif "Shrub" in plants: # If the string is within the temporary table then everything with that string is added.
        shrubs.append(plants)

print(plants)
print(shrubs)
print(flowers)