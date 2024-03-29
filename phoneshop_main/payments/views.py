import stripe
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cart.cart import Cart

# Create your views here.
def HomePageView(request):
    return render(request, 'home.html', {})

def success(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'success.html', {})

def cancelled(request):
    return render(request, 'cancelled.html', {})

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)
    
@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/payments/'
        stripe.api_key = settings.STRIPE_SECRET_KEY

        cart = Cart(request)
        total_amount_pounds = cart.cart_total()

        total_amount_pence = int(total_amount_pounds * 100)

        try:
            # Create new checkout session for the order
            # other optional params include:
            # [billing_address_collection] - displays billing address
            # [customer] - for existing stripe customer ID
            # [payment_intent_data] - capture payment later
            # [customer_email] - prefill email in input form
            # Docs = https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} = redirect will have session ID
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items = [{
                   'price_data': {
                            'currency': 'GBP',
                            'product_data': {
                                'name': 'Total Basket Cost',
                            },
                            'unit_amount': total_amount_pence,
                            },
                    'quantity': 1,
                }],
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    # Handle checkout.session.completed event
    if (event['type'] == 'checkout.session.completed'):
        print('Payment was successful')
        #TODO: we will run the custom code here later
    
    return HttpResponse(status=200)