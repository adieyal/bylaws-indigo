from django.dispatch import receiver
from rest_framework.reverse import reverse

from viewflow.signals import flow_finished
from indigo_workflow.flows import workflow_support
from indigo_slack.slack import send_slack_message


@receiver(flow_finished)
def on_flow_finished(sender, process, task, **kwargs):
    """ Tell slack when a workflow is finished.

    Workflow finished: [Capture amendment information for /za-wc011/act/by-law/2005/refuse-removal](url)
    Country: ZA
    Work: [Foo Work](url)
    """
    workflow_url = workflow_support.flow_url(process)
    summary = process.summary()
    country = process.country
    fields = [{
        "title": "Country",
        "value": country.name,
        "short": "true",
    }]

    if process.locality:
        fields.append({
            "title": "Locality",
            "value": process.locality.name,
            "short": "true",
        })

    work = getattr(process, 'work', None)
    if work:
        work_url = reverse('work', kwargs={'frbr_uri': work.frbr_uri})
        fields.append({
            "title": "Work",
            "value": "<work_url|title>".format(work_url=work_url, title=work.title),
            "short": "false",
        })

    send_slack_message(
        u"Workflow finished: <{url}|{title}>".format(title=summary, url=workflow_url),
        attachments=[{
            "text": summary,
            "fallback": summary,
            "color": "good",
            "fields": fields,
        }]
    )
