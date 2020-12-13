# Sappho Fragment Generation

Uses GPT2 to regenerates missing fragments of Sappho's poetry

**Download model here:**
https://drive.google.com/drive/folders/1-06ovXFjuf9jF72Mv4cd0TvBiCLBJGdi?usp=sharing

**Install gpt-2 simple**

```
pip install -q gpt-2-simple
```
## Poem Generation
```
from SapphoFragments import SapphoGenerator

fragments = ['to Sappho, you', 'in Kypros queen', 'and yet greatly', 'to all on whom the blazing', 'everywhere glory' ,'and you in Acheron’s']

generator = SapphoGenerator(path_to/SapphoGPT2)

poem = generator.generate_poem(fragments)

print(poem)
```

**Output:**
```
to Sappho, you [ love me even sweeter than when I met you
and you have graceless heart against me now
having come to love
I at once flutter and cold sweat covers you
and you anointed yourself.
On the skin
dry] in Kypros queen [ barefoot
mostly hair
fingershot taking
dream of catching
goatherd
hair turned white from head to foot
’O, wake up! Baby! wake up!
’Whoo, wo, wo, wo] and yet greatly [
surpassed beady-handed
Hymenaios!
blest bridegroom, your marriage just as you prayed
has been accomplished
and you have the bride for whom you prayed
gracious your form and your eyes
] to all on whom the blazing [ sun
would seem to me to come
I have a beautiful child
like and a girl like
to the gods
I've known beautiful women before
but one I most especially
believe is wrong
but I simply want to be here] everywhere glory [
and this
superior girl for me --
even to the very very very

beloved -- greatly.

Onward and away
tongue and in voice
imagines
all that good
but I cannot put my] and you in Acheron’s [
dream
like a and then cold sweat covers you
and you in Acheron dream
whirring of ears
you there and high on the heaven
topmost peak
gazing down on the sea
sea and the sound of]
```
