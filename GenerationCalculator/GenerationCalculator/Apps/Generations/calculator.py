from GenerationCalculator.Apps.Generations.models import Generations

def calculate(year):

    generations = Generations.objects.all()
    for gen in generations:
        if gen.from_year<=year<=gen.to_year:
            return gen
    else:
        return "Generation not found :("