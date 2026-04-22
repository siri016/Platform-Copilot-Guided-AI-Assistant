 import random
import string

def handle_referrer(intent, inputs):

    # ── INTENT 1: Refer a Candidate ──
    if intent == 'refer_candidate':
        candidate_name = inputs.get('candidate_name', '')
        job_role = inputs.get('job_role', '')
        relationship = inputs.get('relationship', '')

        if not candidate_name:
            return {
                'insight': 'Please enter Candidate Name',
                'status': 'error',
                'suggestions': ['Enter the full name of the candidate'],
                'actions': ['Try Again']
            }

        ref_id = 'REF' + ''.join(random.choices(string.digits, k=4))

        return {
            'insight': f'Referral Submitted for {candidate_name}!',
            'status': 'success',
            'ref_id': ref_id,
            'suggestions': [
                f'Referral ID: {ref_id} — save this for tracking',
                f'Role applied: {job_role}',
                f'Relationship: {relationship}',
                'HR will review within 3-5 business days'
            ],
            'actions': ['Share Referral ID', 'Refer Another', 'Track Status']
        }

    # ── INTENT 2: Track Referral Status ──
    elif intent == 'track_referral':
        referral_id = inputs.get('referral_id', '')
        candidate_name = inputs.get('candidate_name', '')

        if not referral_id:
            return {
                'insight': 'Please enter your Referral ID',
                'status': 'error',
                'suggestions': ['Enter the Referral ID you received when submitting'],
                'actions': ['Try Again']
            }

        return {
            'insight': f'Referral {referral_id} is Under Review',
            'status': 'pending',
            'suggestions': [
                f'Candidate: {candidate_name}',
                'Stage: Application Screening',
                'Expected update in 3-5 business days',
                'You will be notified on status change'
            ],
            'actions': ['Share Status', 'Download Report']
        }

    # ── INTENT 3: View Referral History ──
    elif intent == 'referral_history':
        time_period = inputs.get('time_period', '')
        status_filter = inputs.get('status_filter', 'All')

        if status_filter == 'Successful':
            total = 3
            success_rate = '100%'
            history = ['REF1001 - Priya Singh - Selected',
                      'REF1002 - Rahul Kumar - Selected',
                      'REF1003 - Amit Shah - Selected']
        elif status_filter == 'Pending':
            total = 2
            success_rate = '0%'
            history = ['REF1004 - Sneha Patel - Under Review',
                      'REF1005 - Ravi Verma - Screening']
        else:
            total = 5
            success_rate = '60%'
            history = ['REF1001 - Priya Singh - Selected',
                      'REF1002 - Rahul Kumar - Selected',
                      'REF1003 - Amit Shah - Selected',
                      'REF1004 - Sneha Patel - Pending',
                      'REF1005 - Ravi Verma - Pending']

        return {
            'insight': f'Total Referrals: {total} | Success Rate: {success_rate}',
            'status': 'success',
            'history': history,
            'suggestions': [
                f'Period: {time_period}',
                f'Total referrals made: {total}',
                f'Success rate: {success_rate}',
                'Keep referring to earn more rewards'
            ],
            'actions': ['Download History', 'Share Report']
        }

    else:
        return {
            'insight': 'Something went wrong',
            'status': 'error',
            'suggestions': ['Please select a valid intent'],
            'actions': ['Go Back']
        }
           