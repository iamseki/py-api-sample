# Python API call

This is a sample project that makes API calls to [International Space Station](https://wheretheiss.at/w/developer) allowing us to get current, past, or future position of the ISS, get timezone information about a set of coordinates. That was proposed by [Daniel Carvalho](https://github.com/danielscarvalho) in the compilers subject at _FTT_.

## Example tsv file :space_invader:

| latitude        | longitude       |maps                                                               
| --------------- | --------------- |------------------------------------------------------------------ |
| -48.44076862751 | 74.769562990861 | https://maps.google.com/maps?q=-48.44076862751,74.769562990861&z=4 |
| -48.44076862751 | 74.769562990861 | https://maps.google.com/maps?q=-48.44076862751,74.769562990861&z=4 |

## Running the project :scroll:

- Just execute `python3 web.py`

The expected output is something like this:

      Tracking international space station:
      It's above us in this location: https://maps.google.com/maps?q=-47.66112210471,72.058616209563&z=4
      Tracking international space station:
      It's above us in this location: https://maps.google.com/maps?q=-47.711897171533,72.225529788978&z=4

> The python process will keep tracking the international space station by aproximately five minutes.
