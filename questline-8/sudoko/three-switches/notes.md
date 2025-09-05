# Three Switches, One Bulb

## 🎯 Problem Statement

There are three switches outside a room, but only one of them controls a light bulb inside the room. I am allowed to enter the room only once and must determine which switch controls the bulb.

## 🧠 Strategy and Logical Steps

1. **Turn ON Switch 1** and leave it ON for a few minutes (2–3 minutes).
2. **Then turn OFF Switch 1** and **immediately turn ON Switch 2**.
3. **Leave Switch 3 OFF** the whole time.
4. Now, **enter the room** and check the bulb:

   - 🔥 **If the bulb is ON**, then **Switch 2** controls the bulb (because it’s currently powering it).
   - ♨️ **If the bulb is OFF but warm**, then **Switch 1** controls the bulb (because it was ON long enough to heat up, but is now off).
   - ❄️ **If the bulb is OFF and cold**, then **Switch 3** controls the bulb (because it was never turned on).

## ✅ Conclusion

Using heat and light as clues, we can logically determine which switch controls the bulb by entering the room only once.

