class Scale(object):
    tones = (
        ('C,G,D,A,E,B,F#,a,e,b,f#,c#,g#,d#', 'C,C#,D,D#,E,F,F#,G,G#,A,A#,B'),
        ('A,F,Bb,Eb,Ab,Db,Gb,d,g,c,f,bb,eb', 'C,Db,D,Eb,E,F,Gb,G,Ab,A,Bb,B'))
    stepsize = { 'm': 1, 'M': 2, 'A': 3 }

    def __init__(self, tonic, intervals=None):
        for tonics, tones in self.tones:
            if tonic in tonics.split(','):
                scale = tones.split(',')
                break
        else:
            raise ValueError("Not a recognized tonic {}".format(tonic))
        initial = t = scale.index(tonic[0].upper() + tonic[1:])
        self.pitches = []
        for i in intervals or  'mmmmmmmmmmmm':
            self.pitches.append(scale[t % len(scale)])
            if len(scale) < t - initial + self.stepsize[i] and i != 'A':
                raise ValueError("Cannot take that stepsize")
            t += self.stepsize[i]
