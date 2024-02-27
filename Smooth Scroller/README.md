<h1> Smooth Scroller
<img src="../Assets/Utility_Badge.png" height=30 align=right>
</h1>

A function to have precise control of the time and distance of a smooth scroll. I use it on my personal website.  

>[!NOTE]
>If fine control over the easing and time is not something that concerns you, I recommend you instead to use either the CSS property ["scroll-behavior: smooth"](https://developer.mozilla.org/en-US/docs/Web/CSS/scroll-behavior) or the window method ["scrollTo"](https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollTo) with its scroll-behavior.

## Parameters of scrollSmooth()
- `distance`  
  - The distance in pixels of where the function will end, if negative will scroll downwards 
- `timeInMs`
  - The total time in milisseconds that will take the scroll to complete, longer times means slower scrolls
  - If the times is lower than the `ms`, it will be equal as `ms`
- `finalOnees`
  - Just before the end, the function will slow down from whatever the speed it is to scroll 1 pixel per iteration
  - The higher this number, more final scrolls will be eased at extreme
  - It cannot be higher than the total scrolls needed to reach destination-2
- `optionalFunction=false`
  - A arbitrary function to be executed when all the scrolls are finished
  - It is optional

## How it works under the hood
Knowing the above you can already use the function without thinking much about it, but if you are interested in how it works:  
First, the function will calculate what is the average scroll power, the total of scrolls needed to reach destination and the "remaining scrolls", that will need to be distributed along the whole scroll "animation".  
(`ms` is also calculated here)

This calculated, it will send these 3 things alongside `finalOnees` to "EaseInOutArray.js" to return an eased array at the beggining and end. More details about this script at the end.

Then the followings variables (most through an object) are passed to a recursive function, that uses `window.setTimeout()` to modify the `body.scrollTop` property by the array numbers each iteration:
- The eased array containing the scroll power for each scroll
- The total number of scrolls
- If the scrolls are downwards
- The optional function, if provided
- ms, after which the function will call itself again (generally 5, the minimum(long story))

And that's it, you reached you destionation! ^^

>[!NOTE]
>To avoid the user from messing with the "scroll animation", manual scrolling is disabled the whole duration (as possible)  
>Re-enabled as soon as all the scrolls finishes

>[!IMPORTANT]
>Use "defer" when using this script, as it needs the page to load first to be able to store the body into a variable

# EaseInOutArray
This function lowers the numbers at its beggining and end, increasing the numbers in its middle for compensation.  
The numbers at the beggining ramp up fastly until they reach the average number.  
The numbers at the beggining descend slowly from the average number
The final numbers are always 1s, determined by the parameter `finalOnees`

Remaining numbers are distributed from the middle to ends  
(It is pretty math-logic heavy, so I dont know how to explain better than this right now)
