import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run():
    #Configuracion del pipeline
    options = PipelineOptions(
        runner="DataflowRunner", # Cambiar a DataflowRunner para GCP o DirectRunner para local
        project="gcp-data-engineer-05",
        region="us-central1",
        temp_location="gs://gcs-bucket-06/temp",
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | "Leer archivo" >> beam.io.ReadFromText("gs://dataflow-samples/shakespeare/kinglear.txt")
            | "Separar palabras" >> beam.FlatMap(lambda line: line.split())
            | "Contar palabras" >> beam.combiners.Count.PerElement()
            | "Guardar resultados" >> beam.io.WriteToText("gs://gcs-bucket-06/output/wordcount")
        )
    print("Template ejecutado exitosamente")

if __name__ == "__main__":
    run()

    