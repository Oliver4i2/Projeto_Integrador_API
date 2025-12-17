import json
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Credential
from .utils.blockchain import blockchain, sha256

@receiver(pre_save, sender=Credential)
def compute_credential_hash(sender, instance: Credential, **kwargs):
    payload = {
        'issuer_did': instance.issuer.did,
        'subject_did': instance.subject.did,
        'type': instance.type,
        'data': instance.data,
        'timestamp': instance.timestamp.isoformat() if instance.timestamp else None,
    }
    instance.hash = sha256(json.dumps(payload, sort_keys=True))

@receiver(post_save, sender=Credential)
def add_credential_to_blockchain(sender, instance: Credential, created, **kwargs):
    if created:
        blockchain.add_block({
            'credential_id': instance.id,
            'issuer_did': instance.issuer.did,
            'subject_did': instance.subject.did,
            'type': instance.type,
            'hash': instance.hash,
            'timestamp': instance.timestamp.isoformat(),
        })
